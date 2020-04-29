import numpy as np
# from astropy.io import fits
# from hst_func import *
import time

# in_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir3/'
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir6pix/'

in_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
out_dir = in_dir
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

    data = np.genfromtxt(in_dir+targname+'_'+filter+'_xy.dat')

    # outName = targname+'_'+filter+'_cut_std_d6_dist.dat'
    outName = targname+'_'+filter+'_cut_std.dat'

    newCol = np.zeros((len(data),6))

    counter = 0
    keptAll = 0
    naSTD = int(0)
    n3STD = int(0)
    for dd in range(len(data)):
        idx = np.array([mag1,mag2,mag3,mag4],dtype=int) # columns of mags

        tmp_std_arr = np.zeros((4))

        arr1 = np.array([data[dd,idx[0]], data[dd,idx[1]], data[dd,idx[2]]]) #3 is out
        arr2 = np.array([data[dd,idx[3]], data[dd,idx[1]], data[dd,idx[2]]]) #0 is out
        arr3 = np.array([data[dd,idx[0]], data[dd,idx[1]], data[dd,idx[3]]]) #2 is out
        arr4 = np.array([data[dd,idx[0]], data[dd,idx[2]], data[dd,idx[3]]]) #1 is out

        mean1 = np.nanmean(arr1)
        mean2 = np.nanmean(arr2)
        mean3 = np.nanmean(arr3)
        mean4 = np.nanmean(arr4)

        std1 = np.nanstd(arr1)
        std2 = np.nanstd(arr2)
        std3 = np.nanstd(arr3)
        std4 = np.nanstd(arr4)

        tmp_std_arr[0] = abs(data[dd,idx[3]] - mean1)/std1
        tmp_std_arr[1] = abs(data[dd,idx[0]] - mean2)/std2
        tmp_std_arr[2] = abs(data[dd,idx[2]] - mean3)/std3
        tmp_std_arr[3] = abs(data[dd,idx[1]] - mean4)/std4

        max_std = np.nanmax(tmp_std_arr)

        num_above_std = (tmp_std_arr >= stdCut).sum()
        num_above_std = int(num_above_std)

        if num_above_std == 2:
            # print('Num Above Std: ', num_above_std)
            naSTD += 1
        if num_above_std > 2:
            n3STD += 1

        if max_std >= stdCut:
            tmp_idx = np.argsort(tmp_std_arr)[::-1][0]
            if tmp_idx == 0:
                newCol[dd,0] = mean1
                newCol[dd,1] = std1
                newCol[dd,2] = dist_std(data,dd,'arr1')
                newCol[dd,3] = 1 # flag cut
                newCol[dd,4] = 3 # idx cut
                counter += 1

            elif tmp_idx == 1:
                newCol[dd,0] = mean2
                newCol[dd,1] = std2
                newCol[dd,2] = dist_std(data,dd,'arr2')
                newCol[dd,3] = 1
                newCol[dd,4] = 0
                counter += 1

            elif tmp_idx == 2:
                newCol[dd,0] = mean3
                newCol[dd,1] = std3
                newCol[dd,2] = dist_std(data,dd,'arr3')
                newCol[dd,3] = 1
                newCol[dd,4] = 2
                counter += 1

            else:
                newCol[dd,0] = mean4
                newCol[dd,1] = std4
                newCol[dd,2] = dist_std(data,dd,'arr4')
                newCol[dd,3] = 1
                newCol[dd,4] = 1
                counter += 1

        else:
            newCol[dd,0] = np.nanmean(data[dd][idx])
            newCol[dd,1] = np.nanstd(data[dd][idx])
            newCol[dd,2] = dist_std(data,dd)
            newCol[dd,3] = 0
            newCol[dd,4] = 4 # means no index was cut
            keptAll += 1

        newCol[dd,5] = num_above_std

    data = np.hstack((data, newCol))

    header = 'RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4 mean stdev pos_std cut_flag idx_cut num_abv_std'

    np.savetxt(out_dir+outName,data,header=header,fmt='%1.5f')

    print('Counter:',counter)
    print('Same: ',keptAll)
    print('Num with 2 above STD: ', naSTD)
    # print('Num with 3 above STD: ', n3STD)
    # print(len(newCol[newCol[:,5] == 2 ]))
    return None

start=time.time()

filterMags('HOROLOGIUM-I','F606W')
filterMags('HOROLOGIUM-I','F814W')

print('It took {0:0.1f} seconds'.format((time.time() - start)))
