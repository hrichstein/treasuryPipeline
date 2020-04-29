import numpy as np
import time


start=time.time()

idxDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
magDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
finalDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'

filters = ['F606W','F814W']

for ff in range(len(filters)):
    # dataFile = np.genfromtxt(magDir+'HOROLOGIUM-I'+"_"+filters[ff]+'_cut_std_d6_dist.dat')
    # idxFile = np.genfromtxt(idxDir+'hor-I-cut_'+filters[ff]+"_match_pix_d6_dist.txt",dtype=int)

    # dataFile = np.genfromtxt(magDir+'HOROLOGIUM-I'+"_"+filters[ff]+'_cut_std.dat')
    # idxFile = np.genfromtxt(idxDir+'hor-I-cut_'+filters[ff]+"_match_pix.txt",dtype=int)

    dataFile = np.genfromtxt(magDir+'HOROLOGIUM-I'+"_"+filters[ff]+'_cut_std.dat')
    idxFile = np.genfromtxt(idxDir+'hor-I-cut_'+filters[ff]+"_match.txt",dtype=int)

    # print(filters[ff])
    # print(max(idxFile))
    outArr = dataFile[idxFile]
    #
    header = 'RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4 mean stdev pos_std cut_flag idx_cut num_abv_std'

    np.savetxt(finalDir+'HOR-I-cut-std_pix_matched_'+filters[ff]+'.dat',outArr,fmt='%1.5f',header=header)
    # counts=len(outArr)
#     fileOut.write('{0} {1:d} \n'.format(targnames[tt],counts))
#
# fileOut.close()
print('It took {0:0.1f} seconds'.format(time.time() - start))
