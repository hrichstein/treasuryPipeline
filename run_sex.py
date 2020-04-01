import numpy as np
import sys
import ast
import os

def run_sex(file):
    coms = np.genfromtxt(file,dtype=str)

    for ss in range(len(coms)):
        s0=' '
        com_in = s0.join(coms[ss])
        # print(com_in)
        res = os.system(com_in)

    return None
