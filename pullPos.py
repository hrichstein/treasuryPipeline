# abandoned to just hard code it in an ipynb

import numpy as np
from astropy.io import fits
from hst_func import *
from flcFuncs import getJdan
import time

workdir = "/Volumes/Spare Data/Hannah_Data/"
catDir = "catRawMags/catDir/"
coordDir = 'mags0811/coordDir/'
magDir = 'mags0811/'

xr, yr, flux, c_star, magr = 0, 1, 2, 3, 4

id, xc, yc, xo, yo, id2, id3, id4 = 5,6,7,8,9,10,11,12

ra_ind, dec_ind = 13,14

def pullRawPos(targname,filter):
    jdanUse = getJdan(targname,filter)

    master = np.loadtxt(workdir+coordDir+targname+"_"+filter+"_coords.txt")

    # coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #working line

    # trying to output xr and yr
    coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #edited

    newCols = np.zeros((len(coordRows),12))

    counter = 0
    for jj in range(len(jdanUse)):
        cat = np.loadtxt(workdir+catDir+jdanUse[jj]+"_"+targname+"_oc.dat",comments='#')

        if jj==0:
            idcol = id
        else:
            idcol = xo+jj+1

        rowsMast = np.transpose(master)

        newIDcol = rowsMast[idcol]
        idx = np.asarray(newIDcol,int)
        #
        reg = cat[idx]

        newCols[:,counter] = reg[:,xr]
        counter += 1
        newCols[:,counter] = reg[:,yr]
        counter += 1
        newCols[:,counter] = reg[:,magr]
        counter += 1

    magList = np.hstack((coordRows, newCols))

    header = 'RA DEC flux c_star xr_1 yr_1 mag1 xr_2 yr_2 mag2 xr_3 yr_3 mag3 xr_4 yr_4 mag4'

    np.savetxt(workdir+magDir+targname+"_"+filter+"_xy.dat", magList, fmt="%1.5f",header=header)

    return None
