import numpy as np
import os


# Calculate median and std for the mags

# directory = "/Volumes/Spare Data/Hannah_Data/mags0811/"
# out_dir = "/Volumes/Spare Data/Hannah_Data/mags0811/"

out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2/'

filename='HOROLOGIUM-I_F814W_xy.dat'


outName = 'HOR-I_F814W_xy_std.dat'

data = np.genfromtxt(out_dir+filename,dtype=float)

newCol = np.zeros((len(data),2))
for dd in range(len(data)):
    idx = np.array([8,13,18,23],dtype=int)
    newCol[dd,0] = np.median(data[dd][idx])
    newCol[dd,1] = np.std(data[dd][idx])

data = np.hstack((data, newCol))

header = 'RA DEC flux c_star xr_1 yr_1 xt_1 yt_1 mag1 xr_2 yr_2 xt_2 yt_2 mag2 xr_3 yr_3 xt_3 yt_3 mag3 xr_4 yr_4 xt_4 yt_4 mag4 median stdev'

# header = 'RA DEC flux c_star xr_1 yr_1 mag1 xr_2 yr_2 mag2 xr_3 yr_3 mag3 xr_4 yr_4 mag4 median stdev'
# header = 'RA DEC mag1 mag2 mag3 mag4 median stdev'

np.savetxt(out_dir+outName,data,header=header,fmt='%1.5f')



# END
