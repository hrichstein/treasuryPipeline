import numpy as np

# inDir = '/Volumes/Spare Data/Hannah_Data/hor1dir1803/dir2503/'

inDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'

name = 'HOR-I'
filter = 'F606W'
mag_high = 24.5
mag_low = 21
std_tol = 0.1
pos_tol = 0.1

data = np.genfromtxt(inDir+name+'-cut-std_pix_matched_'+filter+'.dat',names=True)

keep = data['mean']!=data['mean']
for ll in range(len(data)):
    temp_keep1 = np.logical_and(np.logical_and(data['mean']>=mag_low,\
            data['mean']<=mag_high),np.logical_and(data['pos_std']<pos_tol,\
                                                   data['stdev']<std_tol))

    keep = np.logical_or(keep,temp_keep1)

print(len(data[keep]))
header = 'RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4 mean stdev pos_std cut_flag idx_cut num_abv_std'
#
np.savetxt(inDir+name+'_refStars_'+filter+'.dat', data[keep], fmt='%1.5f', header=header)



#
