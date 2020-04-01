import numpy as np
from spherematch import *
import time

start=time.time()
# targList = 'targnamesDirections.txt'
# magDir = 'mags0811/'
magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir3/'
# names = np.genfromtxt(targList,dtype=str)
# names=['BOOTES-II-NORTH','BOOTES-II-SOUTH','CARINA','DRACO-II']

# for nn in range(len(names)):
infileI = 'HOROLOGIUM-I_F814W_cut_std_new.dat'
infileV = 'HOROLOGIUM-I_F606W_cut_std_new.dat'

xI = np.loadtxt(magDir+infileI, dtype='float')
xV = np.loadtxt(magDir+infileV, dtype='float')

raI = xI[:, 0]
decI = xI[:, 1]
raV = xV[:, 0]
decV = xV[:, 1]

idx1, idx2, ds = spherematch(raI, decI, raV, decV, tol=5e-5, nnearest=1)

outfile = magDir+'hor-I-cut_F814W_match_new_sig.txt'
np.savetxt(outfile, idx1, fmt='%4i')
outfile = magDir+'hor-I-cut_F606W_match_new_sig.txt'
np.savetxt(outfile, idx2, fmt='%4i')

print('It took {0:0.1f} seconds'.format(time.time() - start))
# print('----done !---')
