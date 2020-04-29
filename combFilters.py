import numpy as np

# dire = 'hor1dir0501/' #4 pix
dire = 'hor1dir2804/'

f606w = np.genfromtxt(dire+'HOR-I-cut-std_pix_matched_F606W.dat')
f814w = np.genfromtxt(dire+'HOR-I-cut-std_pix_matched_F814W.dat')

# RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4 mean stdev pos_std cut_flag idx_cut num_abv_std

new_arr = np.hstack((f606w,f814w))

header = "RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w \
mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w \
xt_2_f606w yt_2_f606w \
mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w \
xt_3_f606w yt_3_f606w \
mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w \
xt_4_f606w yt_4_f606w \
mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w \
RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w \
xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w \
mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w \
xt_2_f814w yt_2_f814w \
mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w \
xt_3_f814w yt_3_f814w \
mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w \
xt_4_f814w yt_4_f814w \
mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w"

# save_arr = np.savetxt(dire+"HORI_final_sph_1912.dat",new_arr,header=header,fmt='%1.5f')

save_arr = np.savetxt(dire+"HORI_comb2804.dat",new_arr,header=header,fmt='%1.5f')

# save_arr = np.savetxt(dire+"HORI_pix_0501_d4_dist.dat",new_arr,header=header,fmt='%1.5f')
