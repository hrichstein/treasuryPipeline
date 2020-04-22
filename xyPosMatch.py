import numpy as np
# from scipy.spatial import distance as d
import time

try:
    from scipy.spatial import cKDTree as KDT
except ImportError:
    from scipy.spatial import KDTree as KDT

start=time.time()

# magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/' #4 pix
# magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir6pix/' # 6 pix
# names = np.genfromtxt(targList,dtype=str)
# names=['BOOTES-II-NORTH','BOOTES-II-SOUTH','CARINA','DRACO-II']
# magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir1803/dir2503/'
psfDir = 'mattia/'
flcDir = '/Volumes/Spare Data/Hannah_Data/hor1dir3103/'
matchDir = 'matchXYZ_1604/'

# infileI = 'HOROLOGIUM-I_F814W_CRnoCut_std2.dat'
# infileV = 'HOROLOGIUM-I_F606W_CRnoCut_std2.dat'

infileP = psfDir + 'psf_xyz.dat'
infileF = flcDir + 'flc_xyz.dat'

psfDat = np.loadtxt(infileP, dtype='float')
flcDat = np.loadtxt(infileF, dtype='float')

psfNames= np.genfromtxt(infileP,names=True)
flcNames = np.genfromtxt(infileF,names=True)

matchtol = 2
def distArr(x0,y0,z0,x_arr,y_arr,z_arr):
    dist_arr = np.sqrt( (x0-x_arr)**2 + (y0-y_arr)**2 + (z0-z_arr)**2)

    return dist_arr

########################################################################

x_psf = psfNames['new_x']
y_psf = psfNames['new_y']
z_psf = psfNames['new_z']

x_flc = flcNames['new_x']
y_flc = flcNames['new_y']
z_flc = flcNames['new_z']

coordsP = np.empty((x_psf.size,3))
coordsF = np.empty((x_flc.size,3))

coordsP[:,0] = x_psf
coordsP[:,1] = y_psf
coordsP[:,2] = z_psf

coordsF[:,0] = x_flc
coordsF[:,1] = y_flc
coordsF[:,2] = z_flc

########################################################################

# kdt = KDT(coordsF)
# idxsF = kdt.query(coordsP)[1]
# ds = distArr(x_psf,y_psf,z_psf,x_flc[idxsF],y_flc[idxsF],z_flc[idxsF])


kdt = KDT(coordsP)
idxsP = kdt.query(coordsF)[1]

ds = distArr(x_flc,y_flc,z_flc,x_psf[idxsP],y_psf[idxsP],z_psf[idxsP])

# print(len(ds))

idxsF = np.arange(x_flc.size)

msk = ds < matchtol
idxsF = idxsF[msk]
idxsP = idxsP[msk]
ds = ds[msk]

# print(len(idxs1))


# outfile = magDir+'hor-I-cut_F606W_match_pix.txt'
# np.savetxt(outfile, idxs2, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_F814W_match_pix.txt'
# np.savetxt(outfile, idxs1, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_ds_pix.txt'
# np.savetxt(outfile, ds, fmt='%1.4f')

# outfile = matchDir+'hor-I-cut_F606W_match_pix_noCut2.txt'
# np.savetxt(outfile, idxs2, fmt='%4i')

outfile = matchDir + 'horI-PSF-match.txt'
np.savetxt(outfile, idxsP, fmt='%4i')


outfile = matchDir+'hor-I-FLC_match.txt'
np.savetxt(outfile, idxsF, fmt='%4i')

outfile = matchDir+'hor-I-ds.txt'
np.savetxt(outfile, ds, fmt='%1.4f')

print('It took {0:0.1f} seconds'.format(time.time() - start))








##
