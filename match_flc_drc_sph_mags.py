import numpy as np
import time


start=time.time()
idxDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'

finalDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
drcDir = idxDir
flcDir = idxDir

frames = ['drc','flc']

def match_sph(outpre):

    cats = [drcDir+outpre+'_drc_magCuts.dat',flcDir+outpre+'_flc_magCuts.dat']

    for ff in range(len(frames)):
        dataFile = np.genfromtxt(cats[ff])
        idxFile = np.genfromtxt(idxDir+outpre+'_'+frames[ff]+"_match_0.01_magCuts.dat",dtype=int)

        outArr = dataFile[idxFile]

        print(len(outArr))

        if frames[ff]=='drc':
            header = 'RA_v DEC_v x_v y_v fAper_v fErr_v magAper_v magErr_v magRaw_v magRed_v magAbs_v elong_v ellip_v class_Star_v RA_i DEC_i x_i y_i fAper_i fErr_i magAper_i magErr_i magRaw_i magRed_i magAbs_i elong_i ellip_i class_Star_i corrF_errV corrF_errI corrM_errV corrM_errI'

        else:
            header= 'RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w'

        np.savetxt(finalDir+frames[ff]+'_'+outpre+'_hor1_1em2_magCuts.dat',outArr,fmt='%1.5f',header=header)

    return None

match_sph('upper')
match_sph('lower')

print('It took {0:0.1f} seconds'.format(time.time() - start))
