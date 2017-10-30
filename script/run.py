import os
import sys
import yaml
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.audio import audio
from helper.corpus import corpus
from helper.lexicon import lexicon
from helper.nonsilence_phones import nonsilence_phones
from helper.optional_silence import optional_silence
from helper.silence_phones import silence_phones
from helper.spk2gender import spk2gender
from helper.utt2spk import utt2spk
from helper.wav2scp import wav2scp

if __name__ == '__main__':
    name = "{0}/config/run/context.yaml".format(path)
    context = yaml.load(open(name))
    #audio(context).run()
    #spk2gender(context).run()
    #wav2scp(context).run()
    #utt2spk(context).run()
    #corpus(context).run()
    #lexicon(context).run()
    #nonsilence_phones(context).run()
    #silence_phones(context).run()
    optional_silence(context).run()

