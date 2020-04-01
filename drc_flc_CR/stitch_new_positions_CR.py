import numpy as np

trans_Dir = '/Volumes/Spare Data/Hannah_Data/drc_flc_CR/'
split_Dir = trans_Dir
# split_Dir = '/Volumes/Spare Data/Hannah_Data/hor1dir6pix/'
# New xy positions

# new_up = np.genfromtxt(trans_Dir+'upper_hor1_new_xy.dat')
# new_low = np.genfromtxt(trans_Dir+'lower_hor1_new_xy.dat')

filters=['F606W','F814W']

for ff in range(len(filters)):
    filter = filters[ff]

    new_up = np.genfromtxt(trans_Dir+'upper_hor1_'+filter+'_xy.dat')
    new_low = np.genfromtxt(trans_Dir+'lower_hor1_'+filter+'_xy.dat')

# flc file to tack onto
# flc_old = np.genfromtxt(split_Dir+'HORI_pix_2212_d6_dist.dat')
    if filter=='F606W':
        flc_606_tack = np.genfromtxt(trans_Dir+'HORI_pix_2503_comb.dat')
        concat1 = np.hstack((flc_606_tack, new_up))

        header= "RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w \
        yr_1_f606w xc_1_f606w yc_1_f606w \
        xt_1_f606w yt_1_f606w \
        mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w \
        xt_2_f606w yt_2_f606w \
        mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w \
        xt_3_f606w yt_3_f606w \
        mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w \
        xt_4_f606w yt_4_f606w \
        mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w \
        cut_idx_f606w num_abv_std_f606w \
        RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w \
        xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w \
        mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w \
        xt_2_f814w yt_2_f814w \
        mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w \
        xt_3_f814w yt_3_f814w \
        mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w \
        xt_4_f814w yt_4_f814w \
        mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w \
        cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w"

    else:
        flc_814_tack = np.genfromtxt(trans_Dir+'flc_w_drc_trans_F606W.dat')
        concat1 = np.hstack((flc_814_tack, new_up))

        header= 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w \
        yr_1_f606w xc_1_f606w yc_1_f606w \
        xt_1_f606w yt_1_f606w \
        mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w \
        xt_2_f606w yt_2_f606w \
        mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w \
        xt_3_f606w yt_3_f606w \
        mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w \
        xt_4_f606w yt_4_f606w \
        mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w \
        cut_idx_f606w num_abv_std_f606w \
        RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w \
        xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w \
        mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w \
        xt_2_f814w yt_2_f814w \
        mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w \
        xt_3_f814w yt_3_f814w \
        mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w \
        xt_4_f814w yt_4_f814w \
        mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w \
        cut_idx_f814w num_abv_std_f814w xdrc_up_f606w ydrc_up_f606w xdrc_low_f606w ydrc_low_f606w xdrc_up_f814w ydrc_up_f814w xdrc_low_f814w ydrc_low_f814w'

    concat2 = np.hstack((concat1, new_low))

    np.savetxt(trans_Dir+'flc_w_drc_trans_'+filter+'.dat',concat2,fmt="%1.5f",header=header)
