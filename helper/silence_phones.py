import os
import sys
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.lexicon import lexicon

class silence_phones(lexicon):
    """
    Inherit
    """
