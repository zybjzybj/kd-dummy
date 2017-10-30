import os
import sys
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.copy_egs_local import copy_egs_local

class score(copy_egs_local):
    """
    Inherit
    """
