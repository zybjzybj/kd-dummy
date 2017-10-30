import glob
import os
import ConfigParser
from subprocess import Popen, PIPE
from subprocess import call
import yaml


class spk2gender(object):
    def __init__(self, context):
        self.context = context

    def run(self):
        """
        Split train and test data.
        """
        s_dir = '/work/data' 
        t_root = '/work/kaldi/egs/digits/digits_audio' 
        stn = self.map(s_dir)
        #print(stn)
        # Train data
        data_type = 'train'
        for e in range(9):
            for speaker, src, tgtn in stn:
                if speaker == e: 
                    tgt = "{0}/{1}/{2}".format(t_root, data_type, tgtn)
                    tgt_dir = os.path.dirname(tgt)
                    if not os.path.exists(tgt_dir):
                        os.makedirs(tgt_dir)
                    #print(speaker, src, tgt)
                    self.m4a_to_wav(src, tgt)
        # Test data.
        data_type = 'test'
        for e in [9]:
            for speaker, src, tgtn in stn:
                if speaker == e: 
                    tgt = "{0}/{1}/{2}".format(t_root, data_type, tgtn)
                    tgt_dir = os.path.dirname(tgt)
                    if not os.path.exists(tgt_dir):
                        os.makedirs(tgt_dir)
                    #print(speaker, src, tgt)
                    self.m4a_to_wav(src, tgt)

