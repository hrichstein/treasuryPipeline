import numpy as np
from spherematch import *
import time

dir1='/Volumes/Spare Data/Hannah_Data/mattia/rephotometryquestion/'
psf_file = dir1 + 'HOROLOGIUM_CF.1.TOSEND.CAT'

dir2='/Volumes/Spare Data/Hannah_Data/drc_flc_match/'
my_file = dir2 + 'flc_w_drc_trans814.dat'

idxDir = '/Volumes/Spare Data/Hannah_Data/mattia/'

def run_sph(infile1,infile2,tol=3e-4):

    x1 = np.loadtxt(psf_file, dtype='float')
    x2 = np.loadtxt(my_file, dtype='float')

    ra1 = x1[:, -2]
    dec1 = x1[:, -1]
    ra2 = x2[:, 0]
    dec2 = x2[:, 1]

    idx1, idx2, ds = spherematch(ra1, dec1, ra2, dec2, tol=tol, nnearest=1)

    outfile1 = idxDir+'psf_match.dat'
    np.savetxt(outfile1, idx1, fmt='%4i')
    outfile2 = idxDir+'my_match.dat'
    np.savetxt(outfile2, idx2, fmt='%4i')

    return None

run_sph(psf_file,my_file)
