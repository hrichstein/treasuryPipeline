import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

home_dir ='/Volumes/Spare Data/Hannah_Data/'
d6 = np.genfromtxt(home_dir+'hor1dir6pix/HORI_pix_2212_d6_dist.dat',names=True)
psf = np.genfromtxt(home_dir+'elena_cats/HOROLOGIUM_CF.1.PSF.CAT',names=True)

out_dir = 'mattia/'
newCol = np.zeros((len(d6),6))

##########################################################
keep_606_ = d6['mean_f606w']!=d6['mean_f606w']
for ll in range(len(d6)):
    temp_keep_606_1 = np.logical_and(np.logical_and(d6['mean_f606w']>=21,d6['mean_f606w']<=24.5),
    np.logical_and(d6['pos_std_f606w']<0.5,d6['stdev_f606w']<0.1))
    temp_keep_606_ = np.logical_and(temp_keep_606_1,d6['mean_f606w']-d6['mean_f814w']<-0.3)
    keep_606_ = np.logical_or(keep_606_,temp_keep_606_)

# print(len(d6['mean_f606w'][keep_606_]))

gen_keep_606_ = d6[keep_606_]
print('F606W Kept:',len(gen_keep_606_))
# print( len(gen_keep_606_[abs(gen_keep_606_['cut_idx_f606w']-0) <= 1e-3]))
# print( len(gen_keep_606_[abs(gen_keep_606_['cut_idx_f606w']-1) <= 1e-3]))
# print( len(gen_keep_606_[abs(gen_keep_606_['cut_idx_f606w']-2) <= 1e-3]))
# print( len(gen_keep_606_[abs(gen_keep_606_['cut_idx_f606w']-3) <= 1e-3]))

keep_606_er = gen_keep_606_['mean_f606w']!=gen_keep_606_['mean_f606w']

keep_606_2 = np.logical_and(abs(gen_keep_606_['cut_idx_f606w']-0) >= 1e-3,abs(gen_keep_606_['cut_idx_f606w']-1) >= 1e-3)
keep_606_2 = np.logical_or(keep_606_er,keep_606_2)

keep_606_3 = np.logical_and(abs(gen_keep_606_['cut_idx_f606w']-0) >= 1e-3,abs(gen_keep_606_['cut_idx_f606w']-2) >= 1e-3)
keep_606_3 = np.logical_or(keep_606_er,keep_606_3)

keep_606_4 = np.logical_and(abs(gen_keep_606_['cut_idx_f606w']-0) >= 1e-3,abs(gen_keep_606_['cut_idx_f606w']-3) >= 1e-3)
keep_606_4 = np.logical_or(keep_606_er,keep_606_4)


mean2_1_606 = np.mean(gen_keep_606_['mag1_f606w'][keep_606_2]-gen_keep_606_['mag2_f606w'][keep_606_2])
print(mean2_1_606)

mean3_1_606 = np.mean(gen_keep_606_['mag1_f606w'][keep_606_3]-gen_keep_606_['mag3_f606w'][keep_606_3])
print(mean3_1_606)

mean4_1_606 = np.mean(gen_keep_606_['mag1_f606w'][keep_606_4]-gen_keep_606_['mag4_f606w'][keep_606_4])
print(mean4_1_606)

##########################

keep_814_ = d6['mean_f814w']!=d6['mean_f814w']
for ll in range(len(d6)):
    temp_keep_814_1 = np.logical_and(np.logical_and(d6['mean_f814w']>=21,d6['mean_f814w']<=24.5),
    np.logical_and(d6['pos_std_f814w']<0.5,d6['stdev_f814w']<0.1))
    temp_keep_814_ = np.logical_and(temp_keep_814_1,d6['mean_f606w']-d6['mean_f814w']<-0.3)
    keep_814_ = np.logical_or(keep_814_,temp_keep_814_)

# len(d6['mean_f814w'][keep_814_])

gen_keep_814_ = d6[keep_814_]

print('F814W Kept:',len(gen_keep_814_))
# len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-0) <= 1e-3])
# len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-1) <= 1e-3])
# len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-2) <= 1e-3])
# len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-3) <= 1e-3])


keep_814_er = gen_keep_814_['mean_f814w']!=gen_keep_814_['mean_f814w']
keep_814_2 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3, abs(gen_keep_814_['cut_idx_f814w']-1) >= 1e-3)
keep_814_2 = np.logical_or(keep_814_er,keep_814_2)

keep_814_3 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3, abs(gen_keep_814_['cut_idx_f814w']-2) >= 1e-3)
keep_814_3 = np.logical_or(keep_814_er,keep_814_3)

keep_814_4 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3, abs(gen_keep_814_['cut_idx_f814w']-3) >= 1e-3)
keep_814_4 = np.logical_or(keep_814_er,keep_814_4)

mean2_1_814 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_2]-gen_keep_814_['mag2_f814w'][keep_814_2])
print(mean2_1_814)

mean3_1_814 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_3]-gen_keep_814_['mag3_f814w'][keep_814_3])
print(mean3_1_814)

mean4_1_814 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_4]-gen_keep_814_['mag4_f814w'][keep_814_4])
print(mean4_1_814)

#########################################

newCol[:,0] = d6['mag2_f606w'] + mean2_1_606
newCol[:,1] = d6['mag3_f606w'] + mean3_1_606
newCol[:,2] = d6['mag4_f606w'] + mean4_1_606

newCol[:,3] = d6['mag2_f814w'] + mean2_1_814
newCol[:,4] = d6['mag3_f814w'] + mean3_1_814
newCol[:,5] = d6['mag4_f814w'] + mean4_1_814

d6_col = d6 = np.genfromtxt(home_dir+'hor1dir6pix/HORI_pix_2212_d6_dist.dat')

cat = np.hstack((d6_col,newCol))

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
mag4_f814w mean_f814w stdev_f814w pos_std_f814w cut_flag_f814w cut_idx_f814w num_abv_std_f814w \
mag2_zpt_f606w mag3_zpt_f606w mag4_zpt_f606w \
mag2_zpt_f814w mag3_zpt_f814w mag4_zpt_f814w"

np.savetxt('mag_zpt_cols_2801.dat',cat,header=header,fmt='%1.5f')



#
