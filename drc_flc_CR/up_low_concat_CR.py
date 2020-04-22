import numpy as np


dir_flc = '/Volumes/Spare Data/Hannah_Data/drc_flc_CR/'

frames = ['flc','drc']
filters = ['f606w','f814w']
# positions = ['up','low']
for rr in range(len(frames)):
    if frames[rr]=='flc':
        header = 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w \
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
    else:
        header='RA_v DEC_v x_v y_v fAper_v fErr_v magAper_v magErr_v magRaw_v magRed_v magAbs_v elong_v ellip_v class_Star_v RA_i DEC_i x_i y_i fAper_i fErr_i magAper_i magErr_i magRaw_i magRed_i magAbs_i elong_i ellip_i class_Star_i corrF_errV corrF_errI corrM_errV corrM_errI'

    for ff in range(len(filters)):
        up_arr= np.loadtxt(dir_flc+'up_'+frames[rr]+'_'+filters[ff]+'_matched.dat')
        low_arr= np.loadtxt(dir_flc+'low_'+frames[rr]+'_'+filters[ff]+'_matched.dat')

        concat = np.vstack((up_arr,low_arr))

        np.savetxt(dir_flc+'all_'+frames[rr]+'_'+filters[ff]+'_matched_tol1.dat',concat,header=header)
