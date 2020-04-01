import numpy as np
# from scipy.spatial import distance as d
import time

try:
    from scipy.spatial import cKDTree as KDT
except ImportError:
    from scipy.spatial import KDTree as KDT

start=time.time()

# drcDir = '/Users/hr8jz/Box Sync/Research/source_lists/june13/'
# outDir = '/Volumes/Spare Data/Hannah_Data/drc_flc_match/'

drcDir = '/Volumes/Spare Data/Hannah_Data/drc_flc_CR/'
outDir = '/Volumes/Spare Data/Hannah_Data/drc_flc_CR/'

infileDRC_up = drcDir+'upper_HORI_drc.dat'
infileDRC_low = drcDir+'lower_HORI_drc.dat'
infileFLC = drcDir+'flc_w_drc_trans_F814W.dat'

drc_up = np.genfromtxt(infileDRC_up, names=True)
drc_low = np.genfromtxt(infileDRC_low, names=True)

flc_all = np.genfromtxt(infileFLC, names=True)

matchtol = 5
def distArr(x0,y0,x_arr,y_arr):
    dist_arr = np.sqrt( (x0-x_arr)**2 + (y0-y_arr)**2 )

    return dist_arr

filter = 'f606w'
########################################################################
x_drc_low = drc_low['x_i']
y_drc_low = drc_low['y_i']
xm_flc_low = flc_all['xdrc_low_'+filter]
ym_flc_low = flc_all['ydrc_low_'+filter]

coords1low = np.empty((xm_flc_low.size,2))
coords2low = np.empty((x_drc_low.size,2))

coords1low[:,0] = xm_flc_low
coords1low[:,1] = ym_flc_low

coords2low[:,0] = x_drc_low
coords2low[:,1] = y_drc_low

kdt = KDT(coords2low)
idxs2 = kdt.query(coords1low)[1]

ds = distArr(xm_flc_low,ym_flc_low,x_drc_low[idxs2],y_drc_low[idxs2])

idxs1 = np.arange(xm_flc_low.size)

msk = ds < matchtol
idxs1 = idxs1[msk]
idxs2 = idxs2[msk]
ds = ds[msk]

outfile = outDir+'hor-I-cut_drc_low_'+filter+'_tol5.txt'
np.savetxt(outfile, idxs2, fmt='%4i')

outfile = outDir+'hor-I-cut_flc_low_'+filter+'_tol5.txt'
np.savetxt(outfile, idxs1, fmt='%4i')

outfile = outDir+'hor-I-cut_ds_low_'+filter+'_tol5.txt'
np.savetxt(outfile, ds, fmt='%1.4f')

print('It took {0:0.1f} seconds'.format(time.time() - start))


##############################################
# x_drc_up = drc_up['x_i']
# y_drc_up = drc_up['y_i']
# xm_flc_up = flc_all['xdrc_up_'+filter]
# ym_flc_up = flc_all['ydrc_up_'+filter]
#
# # Need to split these so that the DRC sections are being compared
# # the correct transformed columns
# # 1 will be for the flc
# # first going to do the upper half
# coords1up = np.empty((xm_flc_up.size,2))
# coords2up = np.empty((x_drc_up.size,2))
#
# ################################################
# coords1up[:,0] = xm_flc_up
# coords1up[:,1] = ym_flc_up
#
# coords2up[:,0] = x_drc_up
# coords2up[:,1] = y_drc_up
# ###################################################
#
# kdt = KDT(coords2up)
# idxs2 = kdt.query(coords1up)[1]
#
# ds = distArr(xm_flc_up,ym_flc_up,x_drc_up[idxs2],y_drc_up[idxs2])
#
# idxs1 = np.arange(xm_flc_up.size)
#
# msk = ds < matchtol
# idxs1 = idxs1[msk]
# idxs2 = idxs2[msk]
# ds = ds[msk]
#
# outfile = outDir+'hor-I-cut_drc_up_'+filter+'_tol5.txt'
# np.savetxt(outfile, idxs2, fmt='%4i')
#
# outfile = outDir+'hor-I-cut_flc_up_'+filter+'_tol5.txt'
# np.savetxt(outfile, idxs1, fmt='%4i')
# # # switched naming convention for the 814 filter.
# # # now, name matches with file it should be fed to
# #
# outfile = outDir+'hor-I-cut_ds_up_'+filter+'_tol5.txt'
# np.savetxt(outfile, ds, fmt='%1.4f')
#
# print('It took {0:0.1f} seconds'.format(time.time() - start))








##
