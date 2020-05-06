import numpy as np
from spherematch import *
import time

start=time.time()

idxDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'

def run_sph(outpre,tol=1e-4):

    infile1 = outpre+'_drc.dat'
    infile2 = outpre+'_flc.dat'

    x1 = np.loadtxt(idxDir+infile1, dtype='float')
    x2 = np.loadtxt(idxDir+infile2, dtype='float')

    ra1 = x1[:, 0]
    dec1 = x1[:, 1]
    ra2 = x2[:, 0]
    dec2 = x2[:, 1]

    idx1, idx2, ds = spherematch(ra1, dec1, ra2, dec2, tol=tol, nnearest=1)

    outfile1 = idxDir+outpre+'_drc_match_'+str(tol)+'.dat'
    np.savetxt(outfile1, idx1, fmt='%4i')
    outfile2 = idxDir+outpre+'_flc_match_'+str(tol)+'.dat'
    np.savetxt(outfile2, idx2, fmt='%4i')

    return None

run_sph('upper')
run_sph('lower')

print('It took {0:0.1f} seconds'.format(time.time() - start))
print('----done !---')
