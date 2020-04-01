import numpy as np

# Get DRC magnitudes and tack onto FLC columns

main_dir = '/Volumes/Spare Data/Hannah_Data/drc_flc_match/'

drc_dat = np.genfromtxt(main_dir+'all_drc_814_matched.dat',names=True)
flc_dat = np.genfromtxt(main_dir+'all_flc_814_matched.dat')

newCol = np.zeros((len(flc_dat),2))
newCol[:,0] = drc_dat['magRaw_v']
newCol[:,1] = drc_dat['magRaw_i']

concat = np.hstack((flc_dat,newCol))

header= 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w magDRC_f606w magDRC_f814w'

np.savetxt(main_dir+'flcs_w_drcMAGS.dat',concat,fmt='%1.5f',header=header)
