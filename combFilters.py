import numpy as np

# dire = 'hor1dir0501/' #4 pix
dire = 'hor1dir6pix/'

f606w = np.genfromtxt(dire+'HOR-I-cut-std_pix_matched_F606W_d6_dist.dat')
f814w = np.genfromtxt(dire+'HOR-I-cut-std_pix_matched_F814W_d6_dist.dat')


new_arr = np.hstack((f606w,f814w))

header = "RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xt_1_f606w yt_1_f606w \
mag1_f606w xr_2_f606w yr_2_f606w \
xt_2_f606w yt_2_f606w \
mag2_f606w xr_3_f606w yr_3_f606w \
xt_3_f606w yt_3_f606w \
mag3_f606w xr_4_f606w yr_4_f606w \
xt_4_f606w yt_4_f606w \
mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w \
RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w \
xt_1_f814w yt_1_f814w \
mag1_f814w xr_2_f814w yr_2_f814w \
xt_2_f814w yt_2_f814w \
mag2_f814w xr_3_f814w yr_3_f814w \
xt_3_f814w yt_3_f814w \
mag3_f814w xr_4_f814w yr_4_f814w \
xt_4_f814w yt_4_f814w \
mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w"

# save_arr = np.savetxt(dire+"HORI_final_sph_1912.dat",new_arr,header=header,fmt='%1.5f')

save_arr = np.savetxt(dire+"HORI_pix_2212_d6_dist.dat",new_arr,header=header,fmt='%1.5f')

# save_arr = np.savetxt(dire+"HORI_pix_0501_d4_dist.dat",new_arr,header=header,fmt='%1.5f')
