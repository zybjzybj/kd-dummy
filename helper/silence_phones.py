import os
import sys
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.copy import copy

class silence_phones(copy):
    """
    Inherit
    """
