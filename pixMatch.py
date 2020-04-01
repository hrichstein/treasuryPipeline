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
magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir3103/'
# infileI = 'HOROLOGIUM-I_F814W_cut_std_d6_dist.dat'
# infileV = 'HOROLOGIUM-I_F606W_cut_std_d6_dist.dat'

# infileI = 'HOROLOGIUM-I_F814W_cut_std.dat'
# infileV = 'HOROLOGIUM-I_F606W_cut_std.dat'

infileI = 'HOROLOGIUM-I_F814W_CRnoCut_std2.dat'
infileV = 'HOROLOGIUM-I_F606W_CRnoCut_std2.dat'

f606w = np.loadtxt(magDir+infileI, dtype='float')
f814w = np.loadtxt(magDir+infileV, dtype='float')

print(len(f606w))
print(len(f814w))

matchtol = 2
def distArr(x0,y0,x_arr,y_arr):
    dist_arr = np.sqrt( (x0-x_arr)**2 + (y0-y_arr)**2 )

    return dist_arr

# RA, DEC, flux, c_star, xr_1, yr_1, xt_1, yt_1, mag1, xr_2, yr_2, xt_2, yt_2, mag2, xr_3, yr_3, xt_3, yt_3, mag3, xr_4, yr_4, xt_4, yt_4, mag4, mean, stdev, pos_std, cut_flag, cut_idx, num_abv_std = 0, 1, 2, 3, 4, 5, 6, 7, 8, \
#     9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29

RA, DEC, flux, c_star, xr_1, yr_1, xc_1, yc_1, xt_1, yt_1, mag1, xr_2, yr_2, xc_2, yc_2, xt_2, yt_2, mag2, xr_3, yr_3, xc_3, yc_3, xt_3, yt_3, mag3, xr_4, yr_4, xc_4, yc_4, xt_4, yt_4, mag4, mean, stdev, pos_std, cut_flag, cut_idx, num_abv_std = 0, 1, 2, 3, 4, 5, 6, 7, 8, \
    9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37
########################################################################
xt_f606w = np.vstack((f606w[:,xt_1],f606w[:,xt_2],f606w[:,xt_3],f606w[:,xt_4]))
xt_f814w = np.vstack((f814w[:,xt_1],f814w[:,xt_2],f814w[:,xt_3],f814w[:,xt_4]))

yt_f606w = np.vstack((f606w[:,yt_1],f606w[:,yt_2],f606w[:,yt_3],f606w[:,yt_4]))
yt_f814w = np.vstack((f814w[:,yt_1],f814w[:,yt_2],f814w[:,yt_3],f814w[:,yt_4]))

xm_606 = np.nanmean(xt_f606w,axis=0)
xm_814 = np.nanmean(xt_f814w,axis=0)

ym_606 = np.nanmean(yt_f606w,axis=0)
ym_814 = np.nanmean(yt_f814w,axis=0)

# m_606 = np.hstack((xm_606,ym_606))
# m_814 = np.hstack((xm_814,ym_814))

coords1 = np.empty((xm_606.size,2))
coords2 = np.empty((xm_814.size,2))

coords1[:,0] = xm_606
coords1[:,1] = ym_606

coords2[:,0] = xm_814
coords2[:,1] = ym_814

########################################################################

# matchIds_6 = np.zeros((len(f606w)))
# matchIds_8 = np.zeros((len(f814w)))
#
# master_6 = np.hstack((f606w,matchIds_6))
# master_8 = np.hstack((f814w,matchIds_8))
#
# nF = True
# row = 0
#
# matchrows = infileI
# idx6 = np.arange(0,len(f606w),1)
#
# dist_arr = d.cdist(m_606,m_814)
#
# min606 = np.nanmin(dist_arr,axis=0)
# master_6 = np.hstack((f606w,idx6,min606))

kdt = KDT(coords2)
idxs2 = kdt.query(coords1)[1]

ds = distArr(xm_606,ym_606,xm_814[idxs2],ym_814[idxs2])

idxs1 = np.arange(xm_606.size)

msk = ds < matchtol
idxs1 = idxs1[msk]
idxs2 = idxs2[msk]
ds = ds[msk]

print(len(idxs1))

# outfile = magDir+'hor-I-cut_F606W_match_pix_d6_dist.txt'
# np.savetxt(outfile, idxs2, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_F814W_match_pix_d6_dist.txt'
# np.savetxt(outfile, idxs1, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_ds_pix_d6_dist.txt'
# np.savetxt(outfile, ds, fmt='%1.4f')


# outfile = magDir+'hor-I-cut_F606W_match_pix.txt'
# np.savetxt(outfile, idxs2, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_F814W_match_pix.txt'
# np.savetxt(outfile, idxs1, fmt='%4i')
#
# outfile = magDir+'hor-I-cut_ds_pix.txt'
# np.savetxt(outfile, ds, fmt='%1.4f')

outfile = magDir+'hor-I-cut_F606W_match_pix_noCut2.txt'
np.savetxt(outfile, idxs2, fmt='%4i')

outfile = magDir+'hor-I-cut_F814W_match_pix_noCut2.txt'
np.savetxt(outfile, idxs1, fmt='%4i')

outfile = magDir+'hor-I-cut_ds_pix_noCut2.txt'
np.savetxt(outfile, ds, fmt='%1.4f')

print('It took {0:0.1f} seconds'.format(time.time() - start))








##
