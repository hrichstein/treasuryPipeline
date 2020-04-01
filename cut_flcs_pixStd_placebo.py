import numpy as np
# from astropy.io import fits
# from hst_func import *
import time

# in_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir3/'
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir6pix/'

# in_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir1803/'
out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir3103/'
in_dir = out_dir
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/' # four pixel

RA, DEC, flux, c_star, xr_1, yr_1, xc_1, yc_1, xt_1, yt_1, mag1, xr_2, yr_2, xc_2, yc_2, xt_2, yt_2, mag2, xr_3, yr_3, xc_3, yc_3, xt_3, yt_3, mag3, xr_4, yr_4, xc_4, yc_4, xt_4, yt_4, mag4, mean, stdev, pos_std, cut_flag, cut_idx, num_abv_std = 0, 1, 2, 3, 4, 5, 6, 7, 8, \
    9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37

def dist_std(data,dd,idx_arr=None):

    dd = int(dd)

    if idx_arr=='arr1':
        idx_x = np.array([xt_1,xt_2,xt_3],dtype=int)
        idx_y = np.array([yt_1,yt_2,yt_3],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    elif idx_arr=='arr2':
        idx_x = np.array([xt_4,xt_2,xt_3],dtype=int)
        idx_y = np.array([yt_4,yt_2,yt_3],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))
#124
    elif idx_arr=='arr3':
        idx_x = np.array([xt_1,xt_2,xt_4],dtype=int)
        idx_y = np.array([yt_1,yt_2,yt_4],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))
#134
    elif idx_arr=='arr4':
        idx_x = np.array([xt_1,xt_3,xt_4],dtype=int)
        idx_y = np.array([yt_1,yt_3,yt_4],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    else:
        x_std = np.std(np.array([data[dd,xt_1],data[dd,xt_2],data[dd,xt_3],data[dd,xt_4]]))
        y_std = np.std(np.array([data[dd,yt_1],data[dd,yt_2],data[dd,yt_3],data[dd,yt_4]]))

    dist_std = np.sqrt(x_std**2 + y_std**2)

    return dist_std

def filterMags(targname,filter,stdCut=2.5):

    data = np.genfromtxt(in_dir+targname+'_'+filter+'_xynC.dat')

    # outName = targname+'_'+filter+'_cut_std_d6_dist.dat'
    outName = targname+'_'+filter+'_CRnoCut_std2.dat'

    newCol = np.zeros((len(data),6))

    # counter = 0
    # keptAll = 0
    # naSTD = int(0)
    # n3STD = int(0)
    for dd in range(len(data)):
        idx = np.array([mag1,mag2,mag3,mag4],dtype=int) # columns of mags
    #

    #
    #     else:
        newCol[dd,0] = np.nanmean(data[dd][idx])
        newCol[dd,1] = np.nanstd(data[dd][idx])
        newCol[dd,2] = dist_std(data,dd)
        newCol[dd,3] = 0
        newCol[dd,4] = 4 # means no index was cut
        # keptAll += 1

        # newCol[dd,5] = num_above_std

    data = np.hstack((data, newCol))

    header = 'RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4 mean stdev pos_std cut_flag idx_cut num_abv_std'

    np.savetxt(out_dir+outName,data,header=header,fmt='%1.5f')

    # print('Counter:',counter)
    # print('Same: ',keptAll)
    # print('Num with 2 above STD: ', naSTD)
    # print('Num with 3 above STD: ', n3STD)
    # print(len(newCol[newCol[:,5] == 2 ]))
    return None

start=time.time()

filterMags('HOROLOGIUM-I','F606W')
filterMags('HOROLOGIUM-I','F814W')

print('It took {0:0.1f} seconds'.format((time.time() - start)))
