import os
import sys
path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(path)
from helper.copy_to_root import copy_to_root

class decode(copy_to_root):
    """
    Inherit
    """
