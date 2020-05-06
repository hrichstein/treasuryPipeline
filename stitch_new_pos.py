import numpy as np

main_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'

main_cat = np.genfromtxt(main_dir+'HORI_comb2804.dat')

# new_up_606 = np.genfromtxt(main_dir+'upper_hor1_f606w_xy.dat')
# new_low_606 = np.genfromtxt(main_dir+'lower_hor1_f606w_xy.dat')
#
# new_up_814 = np.genfromtxt(main_dir+'upper_hor1_f814w_xy.dat')
# new_low_814 = np.genfromtxt(main_dir+'lower_hor1_f814w_xy.dat')

new_up_606 = np.genfromtxt(main_dir+'upper_hor1_f606w_xy_magCuts.dat')
new_low_606 = np.genfromtxt(main_dir+'lower_hor1_f606w_xy_magCuts.dat')

new_up_814 = np.genfromtxt(main_dir+'upper_hor1_f814w_xy_magCuts.dat')
new_low_814 = np.genfromtxt(main_dir+'lower_hor1_f814w_xy_magCuts.dat')

concat1 = np.hstack((main_cat, new_up_606))
concat2 = np.hstack((concat1, new_low_606))
concat3 = np.hstack((concat2, new_up_814))
concat4 = np.hstack((concat3, new_low_814))

header = 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w'

np.savetxt(main_dir+'flc_w_drc_trans_all_magCuts.dat',concat4,fmt="%1.5f",header=header)
