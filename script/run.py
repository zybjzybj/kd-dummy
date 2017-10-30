import os
import sys
import yaml
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.audio import audio
from helper.cmd import cmd 
from helper.corpus import corpus
from helper.decode import decode
from helper.lexicon import lexicon
from helper.mfcc import mfcc
from helper.nonsilence_phones import nonsilence_phones
from helper.optional_silence import optional_silence
from helper.pathscript import pathscript
from helper.runscript import runscript
from helper.score import score
from helper.silence_phones import silence_phones
from helper.spk2gender import spk2gender
from helper.steps import steps
from helper.text import text
from helper.utils import utils
from helper.utt2spk import utt2spk
from helper.wav2scp import wav2scp

def run(context):
    """
    context: input context.
    """
    audio(context).run()
    cmd(context).run()
    corpus(context).run()
    decode(context).run()
    lexicon(context).run()
    mfcc(context).run()
    nonsilence_phones(context).run()
    optional_silence(context).run()
    pathscript(context).run()
    runscript(context).run()
    score(context).run()
    silence_phones(context).run()
    spk2gender(context).run()
    steps(context).run()
    text(context).run()
    utils(context).run()
    utt2spk(context).run()
    wav2scp(context).run()

if __name__ == '__main__':
    name = "{0}/config/run/context.yaml".format(path)
    context = yaml.load(open(name))
    run(context)
    
