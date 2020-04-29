# Makes file with positions for each flc for each source

import numpy as np
from astropy.io import fits
from hst_func import *
from flcFuncs import getJdan
import time

workdir = "/Volumes/Spare Data/Hannah_Data/"
# catDir = "catRawMags0501/catDir/"
# coordDir = 'mags0501/coordDir/'
# posDir = '/Volumes/Spare Data/Hannah_Data/positions_d4/'
# magDir = 'mags0811/'
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir0501/'

# CR hor1 stuff
# inner_work = 'hor1flcs/'
catDir = "catRawMags2804/catDir/"
posDir = workdir+catDir # first iteration
# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir1803/'

coordDir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
out_dir = coordDir

xr, yr, flux, c_star, magr = 0, 1, 2, 3, 4

id, xc, yc, xt, yt, id2, id3, id4 = 5,6,7,8,9,10,11,12

ra_ind, dec_ind = 13,14

# For the case of using the offset correction to transform
xo = xt
yo = yt

# header from _coords file : # xr yr flux c_star magr id xc yc xt yt id2 id3 id4 ra dec

def pullRawPos(targname,filter):
    jdanUse = getJdan(targname,filter)

    master = np.loadtxt(coordDir+targname+"_"+filter+"_coords.txt")

    # coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #working line

    # trying to output xr and yr
    coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #edited

    newCols = np.zeros((len(coordRows),28))

    counter = 0
    for jj in range(len(jdanUse)):
        cat = np.loadtxt(posDir+ jdanUse[jj] +"_"+targname+'_'+ filter +"_oc.dat",comments='#')

# xr yr flux c_star magr id xc yc xo yo
        # header of _dc dat: # xr yr flux c_star magr id xc yc
        # up to index 7
        # transformed points
        # cat = np.loadtxt(coordDir+ jdanUse[jj] +"_"+targname+'_'+ filter +"_at.dat",comments='#')

        if jj==0:
            idcol = id
        elif jj==1:
            idcol = id2
        elif jj==2:
            idcol = id3
        else:
            idcol = id4

        rowsMast = np.transpose(master)

        newIDcol = rowsMast[idcol]
        idx = np.asarray(newIDcol,int)
        #
        # print(np.max(idx))
        reg = cat[idx]
    #
        newCols[:,counter] = reg[:,xr]
        counter += 1
        newCols[:,counter] = reg[:,yr]
        counter += 1
        newCols[:,counter] = reg[:,xc]
        counter += 1
        newCols[:,counter] = reg[:,yc]
        counter += 1
        newCols[:,counter] = reg[:,xo]
        counter += 1
        newCols[:,counter] = reg[:,yo]
        counter += 1
        newCols[:,counter] = reg[:,magr]
        counter += 1
    # #
    magList = np.hstack((coordRows, newCols))

    header = 'RA DEC flux c_star xr_1 yr_1 xc_1 yc_1 xt_1 yt_1 mag1 xr_2 yr_2 xc_2 yc_2 xt_2 yt_2 mag2 xr_3 yr_3 xc_3 yc_3 xt_3 yt_3 mag3 xr_4 yr_4 xc_4 yc_4 xt_4 yt_4 mag4'

    np.savetxt(out_dir+targname+"_"+filter+"_xy.dat", magList, fmt="%1.5f",header=header)

    return None
