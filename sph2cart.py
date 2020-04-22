# load files
# add new columns
# use function to turn RA/DEC into Cartesian coords


import numpy as np


def sph2cart(ra,dec):

    r = 80 # kpc

    ra_rad = np.deg2rad(ra)
    dec_rad = np.deg2rad(dec)

    x = r * np.cos(ra_rad) * np.cos(dec_rad)
    y = r * np.sin(ra_rad) * np.cos(dec_rad)
    z = r * np.sin(dec_rad)

    return x, y, z

flc = np.genfromtxt('hor1dir3103/HORI_pix_3103_comb_nC.dat',names=True)
psf = np.genfromtxt('mattia/rephotometryquestion/HOROLOGIUM_CF.1.TOSEND.CAT',names=True)

flc_txt = np.loadtxt('hor1dir3103/HORI_pix_3103_comb_nC.dat')
psf_txt = np.loadtxt('mattia/rephotometryquestion/HOROLOGIUM_CF.1.TOSEND.CAT')

newCol_f = np.zeros((len(flc),3))
newCol_p = np.zeros((len(psf),3))

newCol_f[:,0],newCol_f[:,1],newCol_f[:,2] = sph2cart(flc['RA_f606w'],flc['DEC_f606w'])

newCol_p[:,0],newCol_p[:,1],newCol_p[:,2] = sph2cart(psf['ra'],psf['dec'])

flc2 = np.hstack((flc_txt,newCol_f))
psf2 = np.hstack((psf_txt,newCol_p))

header_f = "RA_f606w DEC_f606w flux_f606w c_star_f606w xr_1_f606w yr_1_f606w xc_1_f606w yc_1_f606w xt_1_f606w yt_1_f606w mag1_f606w xr_2_f606w yr_2_f606w xc_2_f606w yc_2_f606w xt_2_f606w yt_2_f606w mag2_f606w xr_3_f606w yr_3_f606w xc_3_f606w yc_3_f606w xt_3_f606w yt_3_f606w mag3_f606w xr_4_f606w yr_4_f606w xc_4_f606w yc_4_f606w xt_4_f606w yt_4_f606w mag4_f606w mean_f606w stdev_f606w pos_std_f606w cut_flag_f606w cut_idx_f606w num_abv_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w xr_1_f814w yr_1_f814w xc_1_f814w yc_1_f814w xt_1_f814w yt_1_f814w mag1_f814w xr_2_f814w yr_2_f814w xc_2_f814w yc_2_f814w xt_2_f814w yt_2_f814w mag2_f814w xr_3_f814w yr_3_f814w xc_3_f814w yc_3_f814w xt_3_f814w yt_3_f814w mag3_f814w xr_4_f814w yr_4_f814w xc_4_f814w yc_4_f814w xt_4_f814w yt_4_f814w mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w new_x new_y new_z"

header_p = "x y m606c m814c nstar sat606 sat814 camera m606 s606 q606 o606 f606 g606 rxs606 sky606 rmssky606 m814 s814 q814 o814 f814 g814 rxs814 sky814 rmssky814 ra dec new_x new_y new_z"

np.savetxt('hor1dir3103/flc_xyz.dat',flc2, fmt='%1.5f', header=header_f)

np.savetxt('mattia/psf_xyz.dat',psf2,fmt='%1.5f', header=header_p)
