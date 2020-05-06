import numpy as np

save_dir = 'hor1dir2804/'

drc_dir = '/Users/hr8jz/Box Sync/Research/source_lists/june13/'
drc_source_list=np.genfromtxt(drc_dir + 'HOROLOGIUM-I_sfErr.dat',names=True)

flc_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
flc_source_list = np.genfromtxt(flc_dir+'HORI_comb2804.dat',names=True)

###############################################################################
y_drc = drc_source_list['y_v']
upper_drc = drc_source_list[y_drc > 2231]
lower_drc = drc_source_list[y_drc < 2032]

ud = np.logical_and(upper_drc['magRaw_i']>22.5,upper_drc['magRaw_i']<25)
ld = np.logical_and(lower_drc['magRaw_i']>22.5,lower_drc['magRaw_i']<25)

header_drc = '# RA_v DEC_v x_v y_v fAper_v '\
'fErr_v magAper_v magErr_v magRaw_v magRed_v '\
'magAbs_v elong_v ellip_v class_Star_v RA_i DEC_i x_i '\
'y_i fAper_i fErr_i magAper_i magErr_i magRaw_i magRed_i '\
'magAbs_i elong_i ellip_i class_Star_i corrF_errV corrF_errI '\
'corrM_errV corrM_errI'

np.savetxt(save_dir+'upper_drc_magCuts.dat',upper_drc[ud],header=header_drc)
np.savetxt(save_dir+'lower_drc_magCuts.dat',lower_drc[ld],header=header_drc)

###############################################################################

y_flc = flc_source_list['yr_1_f606w']
upper_flc = flc_source_list[y_flc > 2053]
lower_flc = flc_source_list[y_flc < 2043]

uf = np.logical_and(upper_flc['mean_f814w']>22.5,upper_flc['mean_f814w']<25)
lf = np.logical_and(lower_flc['mean_f814w']>22.5,lower_flc['mean_f814w']<25)

header_flc = 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w'


np.savetxt(save_dir+'upper_flc_magCuts.dat',upper_flc[uf],header=header_flc)
np.savetxt(save_dir+'lower_flc_magCuts.dat',lower_flc[lf],header=header_flc)
