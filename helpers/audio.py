import glob
import os
import ConfigParser
from subprocess import Popen, PIPE
from subprocess import call
import yaml


class audio(object):
    def __init__(self, context):
        self.context = context

    def map(self, sdir):
        """
        Map .m4a file names into .wav file names
        sdir: source directory containing .m4a files.
        return: A list of .m4a, .wav names.
        """
        result = []
        # Do all two digit patterns.
        for i in range(10)[1:]:
            for j in range(10):
                pattern ='{0}/*({1}{2})*'.format(sdir, i, j)
                if j == 0:
                   s = i - 1
                   e = 9
                else:
                   s = i
                   e = j - 1
                tgt ='{0}/1_{1}_{2}.wav'.format(s, s, e)
                src = glob.glob(pattern)
                result.append((s, src[0], tgt))
         # Do [2-9]
        for j in range(2, 10):
            pattern ='{0}/*({1})*'.format(sdir, j)
            tgt ='0/1_0_{0}.wav'.format(j-1)
            src = glob.glob(pattern)
            result.append((0, src[0], tgt))
        # Do ffirst one.      
        pattern ='{0}/Recording.m4a'.format(sdir)
        tgt ='0/1_0_0.wav'
        src = glob.glob(pattern)
        result.append((0, src[0], tgt))
        # Do last one.      
        pattern ='{0}/*(100)*'.format(sdir)
        tgt ='9/1_9_9.wav'
        src = glob.glob(pattern)
        result.append((9, src[0], tgt))
        return result

    def m4a_to_wav(self, src, tgt):
        """
        Transform src to tgt using faad.
        src: .m4a file.
        tgt: .wav file.
        return: rc, out, err
        """
        args = ["faad", "-o", "{0}".format(tgt), "{0}".format(src)]
        pipe = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        out, err = pipe.communicate()
        rc = pipe.returncode
        return rc, out, err

    def transform(self):
        """
        Split train and test data.
        """
        s_dir = self.context['audio']['source']['dir']
        t_root = '{0}/{1}'.format(self.context['egs']['root'], self.context['audio']['target']['dir'])
        stn = self.map(s_dir)
        #print(stn)
        # Train data
        for k, v in self.context['data']['split'].items():
            for e in v:
                for speaker, src, tgtn in stn:
                    if speaker == e: 
                        tgt = "{0}/{1}/{2}".format(t_root, k, tgtn)
                        tgt_dir = os.path.dirname(tgt)
                        if not os.path.exists(tgt_dir):
                            os.makedirs(tgt_dir)
                        #print(speaker, src, tgt)
                        self.m4a_to_wav(src, tgt)

    def run(self):
        """
        """
        self.transform()

