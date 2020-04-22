import numpy as np
import time

start=time.time()

psfDir = 'mattia/'
flcDir = '/Volumes/Spare Data/Hannah_Data/hor1dir3103/'
matchDir = 'matchXYZ_1604/'

dataFile = np.genfromtxt(psfDir+'psf_xyz.dat')
idxFile = np.genfromtxt(matchDir+'horI-PSF-match.txt',dtype='int')

outArr = dataFile[idxFile]
header = 'x y m606c m814c nstar sat606 sat814 camera m606 s606 q606 o606 f606 g606 rxs606 sky606 rmssky606 m814 s814 q814 o814 f814 g814 rxs814 sky814 rmssky814 ra dec new_x new_y new_z'

np.savetxt(matchDir+'matched_psf_xyz.dat',outArr,fmt='%1.5f',header=header)

dF2 = np.genfromtxt(flcDir+'flc_xyz.dat')
idxF2 = np.genfromtxt(matchDir+'hor-I-FLC_match.txt',dtype='int')
outA2 = dF2[idxF2]

head2 = "RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w new_x new_y new_z"

np.savetxt(matchDir+'matched_flc_xyz.dat',outA2,fmt='%1.5f',header=head2)

print('It took {0:0.1f} seconds'.format(time.time() - start))

# End
