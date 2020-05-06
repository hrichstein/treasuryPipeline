import numpy as np
from scipy import stats

main_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
# Difference is just which pixel positions (from which filter) were used to match
f606w = np.genfromtxt(main_dir+'flcs_w_drcMAGS_f606w.dat',names=True)
f814w = np.genfromtxt(main_dir+'flcs_w_drcMAGS_f814w.dat',names=True)

cat = np.genfromtxt('hor1dir2804/flc_w_drc_trans_all.dat',names=True)
cat_all = np.loadtxt('hor1dir2804/flc_w_drc_trans_all.dat')

# Calculating what additive correction factor is needed for each filter
flcA_diff_arr_606 = stats.sigmaclip(f814w['magDRC_f606w']-f814w['mean_f606w'],2.5,2.5)

flcA_diff_arr_814 = stats.sigmaclip(f814w['magDRC_f814w']-f814w['mean_f814w'],2.5,2.5)

# the zero is because sigmaclip gives back extra stuff
magA_606_corr = np.nanmean(flcA_diff_arr_606[0])
magA_814_corr = np.nanmean(flcA_diff_arr_814[0])

# The stdev/root(N) to be added in quadrature to original error
f814w_err_add = np.std(flcA_diff_arr_814[0])/np.sqrt(len(flcA_diff_arr_814[0]))
f606w_err_add = np.std(flcA_diff_arr_606[0])/np.sqrt(len(flcA_diff_arr_606[0]))

new_f814w_err = np.sqrt(cat['stdev_f814w']**2 + f814w_err_add**2)
new_f606w_err = np.sqrt(cat['stdev_f606w']**2 + f606w_err_add**2)

# Making the new columns to add
newCol = np.zeros((len(cat),4))
newCol[:,0] = cat['mean_f606w'] + magA_606_corr
newCol[:,1] = cat['mean_f814w'] + magA_814_corr
newCol[:,2] = new_f606w_err
newCol[:,3] = new_f814w_err

concat = np.hstack((cat_all,newCol))

header= 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w magZPT_f606w magZPT_f814w errZPT_f606w errZPT_f814w'

np.savetxt(main_dir+'zpt_flcs_0605.dat',concat,fmt='%1.5f',header=header)
