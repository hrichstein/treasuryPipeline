import numpy as np
# from astropy.io import fits
# from hst_func import *
import time

in_dir = '/Volumes/Spare Data/Hannah_Data/mattia/'
out_dir = '/Volumes/Spare Data/Hannah_Data/mattia/'
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/' # four pixel
def dist_std(data,dd,idx_arr=None):

    dd = int(dd)

    if idx_arr=='arr1':
        idx_x = np.array([6,11,16],dtype=int)
        idx_y = np.array([7,12,17],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    elif idx_arr=='arr2':
        idx_x = np.array([21,11,16],dtype=int)
        idx_y = np.array([22,12,17],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    elif idx_arr=='arr3':
        idx_x = np.array([6,11,21],dtype=int)
        idx_y = np.array([7,12,22],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    elif idx_arr=='arr4':
        idx_x = np.array([6,16,21],dtype=int)
        idx_y = np.array([7,17,22],dtype=int)
        x_std = np.std(np.array([data[dd,idx_x[0]],data[dd,idx_x[1]],data[dd,idx_x[2]]]))
        y_std = np.std(np.array([data[dd,idx_y[0]],data[dd,idx_y[1]],data[dd,idx_y[2]]]))

    else:
        x_std = np.std(np.array([data[dd,6],data[dd,11],data[dd,16],data[dd,21]]))
        y_std = np.std(np.array([data[dd,7],data[dd,12],data[dd,17],data[dd,22]]))

    dist_std = np.sqrt(x_std**2 + y_std**2)

    return dist_std

################################################################

def filterMags(targname,filter,stdCut=2.5):

    # data = np.genfromtxt(in_dir+targname+'_'+filter+'_xy.dat')

    data = np.genfromtxt(in_dir+'mag_zpt_cols_2801.dat')
    # outName = targname+'_'+filter+'_cut_std_d6_dist.dat'
    # outName = targname+'_mag_zpt_std_2301.dat'

    newCol = np.zeros((len(data),6))

    counter = 0
    keptAll = 0
    naSTD = int(0)
    n3STD = int(0)

    if filter=='F606W':
        data = np.genfromtxt(in_dir+'mag_zpt_cols_2801.dat')
        outName = targname+'_mag_zpt_std_606_2801.dat'

        idx = np.array([8,60,61,62],dtype=int) # columns of mags

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
        mag2_zpt_f814w mag3_zpt_f814w mag4_zpt_f814w zpt_mean_f606w\
        zpt_std_f606w zpt_pos_std_f606w zpt_cut_f606w zpt_idx_f606w\
        zpt_abv_std_f606w"

    else:
        data = np.genfromtxt(in_dir+targname+'_mag_zpt_std_606_2801.dat')
        outName = targname+'_mag_zpt_std_all_2801.dat'

        idx = np.array([38,63,64,65],dtype=int)
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
        mag2_zpt_f814w mag3_zpt_f814w mag4_zpt_f814w zpt_mean_f606w\
        zpt_std_f606w zpt_pos_std_f606w zpt_cut_f606w zpt_idx_f606w\
        zpt_abv_std_f606w \
        zpt_mean_f814w\
        zpt_std_f814w zpt_pos_std_f814w zpt_cut_f814w zpt_idx_f814w\
        zpt_abv_std_f814w "

    for dd in range(len(data)):

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
