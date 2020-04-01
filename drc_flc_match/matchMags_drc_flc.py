import numpy as np
import time


start=time.time()
# idxDir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/'
# magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/'
# finalDir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/'

idxDir = '/Volumes/Spare Data/Hannah_Data/drc_flc_match/'
magDir = './'
finalDir = './'

# filters = ['F606W','F814W']
drcDir = '/Users/hr8jz/Box Sync/Research/source_lists/june13/'
# for ff in range(len(filters)):
dataFile = np.genfromtxt(magDir+'flc_w_drc_trans814.dat')
# dataFile = np.genfromtxt(magDir+'all_flc_pix_matched.dat')
idxFile = np.genfromtxt(idxDir+'hor-I-cut_flc_low_814_tol5.txt',dtype=int)

# dataFile = np.genfromtxt(drcDir+'lower_HORI.dat')
# idxFile = np.genfromtxt(idxDir+'hor-I-cut_drc_low_814_tol5.txt',dtype=int)

# dataFile = np.genfromtxt(drcDir+'upper_HORI.dat')
# idxFile = np.genfromtxt(idxDir+'hor-I-cut_drc_up_814_tol5.txt',dtype=int)

# print(filters[ff])
# print(max(idxFile))
outArr = dataFile[idxFile]
#
header = 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w'

# header='RA_v DEC_v x_v y_v fAper_v fErr_v magAper_v magErr_v magRaw_v magRed_v magAbs_v elong_v ellip_v class_Star_v RA_i DEC_i x_i y_i fAper_i fErr_i magAper_i magErr_i magRaw_i magRed_i magAbs_i elong_i ellip_i class_Star_i corrF_errV corrF_errI corrM_errV corrM_errI'

np.savetxt(finalDir+'low_flc_814_matched.dat',outArr,fmt='%1.5f',header=header)
# counts=len(outArr)
#     fileOut.write('{0} {1:d} \n'.format(targnames[tt],counts))
#
# fileOut.close()
print('It took {0:0.1f} seconds'.format(time.time() - start))

#######################
