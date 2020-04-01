import numpy as np
from spherematch import *
import time

# start=time.time()
# targList = 'targnamesDirections.txt'
# magDir = 'mags0811/magDir/'
dir1='/Users/hr8jz/Box Sync/Research/source_lists/june13/'
dir2='/Volumes/Spare Data/Hannah_Data/hor1dir6pix/'
idxDir = '/Volumes/Spare Data/Hannah_Data/drc_flc_match/'
# names = np.genfromtxt(targList,dtype=str)
# names=['BOOTES-II-NORTH','BOOTES-II-SOUTH','CARINA','DRACO-II']
# infile1 = '/Users/hr8jz/Box Sync/Research/source_lists/june13/HOROLOGIUM-I_sfErr.dat'  #drc
# infile2 = '/Volumes/Spare Data/Hannah_Data/hor1dir6pix/HORI_pix_2212_d6_dist.dat' #flcs
# for nn in range(len(names)):
def run_sph(infile1,infile2,outpre,tol=1e-4):

    x1 = np.loadtxt(dir1+infile1, dtype='float')
    x2 = np.loadtxt(dir2+infile2, dtype='float')

    ra1 = x1[:, 0]
    dec1 = x1[:, 1]
    ra2 = x2[:, 0]
    dec2 = x2[:, 1]

    idx1, idx2, ds = spherematch(ra1, dec1, ra2, dec2, tol=tol, nnearest=1)

    outfile1 = idxDir+outpre+'_drc_match_1e4.dat'
    np.savetxt(outfile1, idx1, fmt='%4i')
    outfile2 = idxDir+outpre+'_flc_match_1e4.dat'
    np.savetxt(outfile2, idx2, fmt='%4i')

    return None
# print('It took {0:0.1f} seconds'.format(time.time() - start))
# print('----done !---')
