import numpy as np

idxDir = '/Volumes/Spare Data/Hannah_Data/mattia/'

dir1='/Volumes/Spare Data/Hannah_Data/mattia/rephotometryquestion/'
dir2='/Volumes/Spare Data/Hannah_Data/drc_flc_match/'

psf_file = dir1 + 'HOROLOGIUM_CF.1.TOSEND.CAT'
my_file = dir2 + 'flc_w_drc_trans814.dat'

# idx files
# my_match.dat
# psf_match.dat

# dataFile = np.genfromtxt(my_file)
# idxFile = np.genfromtxt(idxDir + 'my_match.dat',dtype=int)
#
# header= 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w'
#
# outArr = dataFile[idxFile]
#
# np.savetxt(idxDir+'matched_myphot.dat',outArr,fmt='%1.5f',header=header)

dataFile = np.genfromtxt(psf_file)
idxFile = np.genfromtxt(idxDir + 'psf_match.dat',dtype=int)

header= 'x y m606c m814c  nstarsat606sat814camera m606 s606 q606 o606 f606 g606 rxs606 sky606 rmssky606 m814 s814 q814 o814 f814 g814 rxs814 sky814 rmssky814 ra dec'

outArr = dataFile[idxFile]

np.savetxt(idxDir+'matched_psfphot.dat',outArr,fmt='%1.5f',header=header)
