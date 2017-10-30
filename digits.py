import glob
import os
import ConfigParser
from subprocess import Popen, PIPE
from subprocess import call
import yaml


class audio(object):
    def __init__(self, context):
        self.context = context

    def map(self, sdir, tdir):
        """
        Map .m4a file names into .wav file names
        sdir: source directory containing .m4a files.
        tdir: target directory containing .wav files.
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
                tgt ='{0}/1_{1}_{2}.wav'.format(tdir, s, e)
                src = glob.glob(pattern)
                result.append((src[0], tgt))
         # Do [2-9]
        for j in range(2, 10):
            pattern ='{0}/*({1})*'.format(sdir, j)
            tgt ='{0}/1_0_{1}.wav'.format(tdir, j-1)
            src = glob.glob(pattern)
            result.append((src[0], tgt))
        # Do ffirst one.      
        pattern ='{0}/Recording.m4a'.format(sdir)
        tgt ='{0}/1_0_0.wav'.format(tdir)
        src = glob.glob(pattern)
        result.append((src[0], tgt))
        # Do last one.      
        pattern ='{0}/*(100)*'.format(sdir)
        tgt ='{0}/1_9_9.wav'.format(tdir)
        src = glob.glob(pattern)
        result.append((src[0], tgt))
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

    def transform(self, src_tgt):
        """
        Transform m4a into wav in batch.
        src_tgt: list of src and tgt names.
        """
        for src, tgt in src_tgt:
            rc, out, err = self.m4a_to_wav(src, tgt)
            if not rc:
                print("Failed for {0} {1}".format(src, tgt))

    def run(self):
        """
        """
        sdir = '/work/data' 
        tdir = '/work/kaldi/egs/digits/digits_audio' 
        src_tgt = self.map(sdir, tdir)
        print(src_tgt)
 
if __name__ == '__main__':
    name = "context.yaml"
    context = yaml.load(open(name))
    a = audio(context)
    a.run()
