# superseded by cut_flcs_pixStd.py

import numpy as np
# from astropy.io import fits
# from hst_func import *
import time

out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/'

def filterMags(targname,filter,stdCut=2.5):

    data = np.genfromtxt(out_dir+targname+'_'+filter+'_xy.dat')

    outName = targname+'_'+filter+'_cut_std_d4.dat'

    newCol = np.zeros((len(data),5))

    counter = 0
    keptAll = 0
    naSTD = int(0)
    n3STD = int(0)
    for dd in range(len(data)):
        idx = np.array([8,13,18,23],dtype=int) # columns of mags

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
        if num_above_std > 1:
            # print('Num Above Std: ', num_above_std)
            naSTD += 1
        if num_above_std > 2:
            n3STD += 1

        if max_std >= stdCut:
            tmp_idx = np.argsort(tmp_std_arr)[::-1][0]
            if tmp_idx == 0:
                newCol[dd,0] = mean1
                newCol[dd,1] = std1
                newCol[dd,2] = 1 # flag cut
                newCol[dd,3] = 3 # idx cut
                counter += 1

            elif tmp_idx == 1:
                newCol[dd,0] = mean2
                newCol[dd,1] = std2
                newCol[dd,2] = 1
                newCol[dd,3] = 0
                counter += 1

            elif tmp_idx == 2:
                newCol[dd,0] = mean3
                newCol[dd,1] = std3
                newCol[dd,2] = 1
                newCol[dd,3] = 2
                counter += 1

            else:
                newCol[dd,0] = mean4
                newCol[dd,1] = std4
                newCol[dd,2] = 1
                newCol[dd,3] = 1
                counter += 1

        else:
            newCol[dd,0] = np.nanmean(data[dd][idx])
            newCol[dd,1] = np.nanstd(data[dd][idx])
            newCol[dd,2] = 0
            newCol[dd,3] = 4 # means no index was cut
            keptAll += 1

        newCol[dd,4] = num_above_std
        # if abs(data[dd,idx[3]] - mean1) >= (3.0*std1):
        #     newCol[dd,0] = mean1
        #     newCol[dd,1] = std1
        #     newCol[dd,2] = 1
        #     newCol[dd,3] = 3
        #     counter += 1
        #
        # elif abs(data[dd,idx[0]] - mean2) >= (3.0*std2):
        #     newCol[dd,0] = mean2
        #     newCol[dd,1] = std2
        #     newCol[dd,2] = 1
        #     newCol[dd,3] = 0
        #     counter += 1
        #
        # elif abs(data[dd,idx[2]] - mean3) >= (3.0*std3):
        #     newCol[dd,0] = mean3
        #     newCol[dd,1] = std3
        #     newCol[dd,2] = 1
        #     newCol[dd,3] = 2
        #     counter += 1
        #
        # elif abs(data[dd,idx[1]] - mean4) >= (3.0*std4):
        #     newCol[dd,0] = mean4
        #     newCol[dd,1] = std4
        #     newCol[dd,2] = 1
        #     newCol[dd,3] = 1
        #     counter += 1
        #
        # else:
        #     newCol[dd,0] = np.mean(data[dd][idx])
        #     newCol[dd,1] = np.std(data[dd][idx])
        #     newCol[dd,2] = 0
        #     newCol[dd,3] = 4
        #     keptAll += 1

    data = np.hstack((data, newCol))

    header = 'RA DEC flux c_star xr_1 yr_1 xt_1 yt_1 mag1 xr_2 yr_2 xt_2 yt_2 mag2 xr_3 yr_3 xt_3 yt_3 mag3 xr_4 yr_4 xt_4 yt_4 mag4 mean stdev cut_flag idx_cut num_abv_std'

    np.savetxt(out_dir+outName,data,header=header,fmt='%1.5f')

    print('Counter:',counter)
    print('Same: ',keptAll)
    print('Num with 2 above STD: ', naSTD)
    print('Num with 3 above STD: ', n3STD)
    return None

start=time.time()

filterMags('HOROLOGIUM-I','F606W')
filterMags('HOROLOGIUM-I','F814W')

print('It took {0:0.1f} seconds'.format((time.time() - start)))
