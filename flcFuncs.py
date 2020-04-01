import numpy as np
from astropy.io import fits
from hst_func import *
from astropy import wcs
import time

workdir = "/Volumes/Spare Data/Hannah_Data/"
catDir = "catRawMags/catDir/"
coordDir = 'mags0811/coordDir/'
magDir = 'mags0811/magDir/'

xr, yr, flux, c_star, magr = 0, 1, 2, 3, 4

id, xc, yc, xo, yo, id2, id3, id4 = 5,6,7,8,9,10,11,12

ra_ind, dec_ind = 13,14

# fmt = "%1.5f %1.5f %1.5f %1.4 %1.5f %1.5f %1.5f %1.5f %d %d %d"
fmt = "%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f %d %d %d"

matchtol = 2.0 #20 pixels arcsec

def getJdan(targname,filter):

    jdanList_file = np.loadtxt(workdir+targname+"_flcs.txt",dtype="<U50")

    jdan = jdanList_file[:,0]
    jdanFilter = jdanList_file[:,1]

    jdanUse = []
    for jj in range(len(jdan)):
        if jdanFilter[jj]==filter:
            jdanUse.append(jdan[jj])

    jdanUse = np.array(jdanUse)

    return jdanUse

# Distortion correction done on the WJC images

def distCor(targname,filter):

    jdanUse = getJdan(targname,filter)

    for ff in range(len(jdanUse)):
        #Load catalog
        cat = np.loadtxt(workdir+"catRawMags/" + jdanUse[ff]+'_'+targname+'_'+filter+'_wMag.dat')

        #Do correction
        cor = acsDistortion(workdir+'wfc_'+filter,cat[:,xr],cat[:,yr])

        #Add columns
        cat = np.hstack((cat,cor))

        header = 'xr yr flux c_star magr id xc yc'

        np.savetxt(workdir+catDir+jdanUse[ff]+'_'+targname+'_'+filter+'_dc.dat',cat,fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f",header=header)

    return None

# Offset correction

def offCor(targname,filter):

    jdanUse = getJdan(targname,filter)

    offset = 20.0

    # Begin Loop

    for ff in range(len(jdanUse)):

    ## Load images, retrieve offset info
        tempim = fits.open(workdir+'flc_fits/'+jdanUse[ff]+"_flc.fits")
        xoff = float(tempim[0].header["POSTARG1"])
        yoff = float(tempim[0].header["POSTARG2"])

    # Load the respective catalog
        cat = np.loadtxt(workdir+catDir+jdanUse[ff]+"_"+targname+"_"+filter+"_dc.dat")

        # Create an array for the new values
        newCol = np.zeros((len(cat),2))

        # Apply offsets to columns
        newCol[:,0] = cat[:,xc] - (offset * xoff)
        newCol[:,1] = cat[:,yc] - (offset * yoff)

        # Combine to single array and save out
        cat = np.hstack((cat, newCol))

        header =  "xr yr flux c_star magr id xc yc xo yo"

        # Save each WJC with new columns of offsets
        np.savetxt(workdir +catDir+ jdanUse[ff] + "_"+targname+"_oc.dat", cat, fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f", header=header)

    return None
# Matching time

def matchWJCs(targname,filter,matchtol=matchtol):

    jdanUse = getJdan(targname,filter)

    master = np.loadtxt(workdir+catDir+jdanUse[0] +"_"+targname+"_oc.dat")

    # Create an array of zeros with columns equal to the number of non-master dithers to store the matching id for each source

    matchids = np.zeros((len(master), (len(jdanUse)-1)))

    master = np.hstack((master, matchids))

    # Loop through other images

    for dd in range(len(jdanUse)-1):

        # Load catalogs

        cat = np.loadtxt(workdir+catDir+jdanUse[dd+1]+"_"+targname+"_oc.dat")

        nF = True
        row = 0

        while (nF): #notFinished

            matchrows = cat[(abs(master[row][xo] - cat[:,xo]) <= matchtol) & (abs(master[row][yo] - cat[:,yo]) <= matchtol)]

            # Setting the proper column number to the matching index.
            if (len(matchrows) == 1):
              master[row][xo+dd+2] = matchrows[0][id]
              row = row + 1

            elif (len(matchrows) > 1):
                # print("more than one source")
                # print(len(matchrows))

                magDif = np.zeros((len(matchrows),1))
                for mm in range(len(matchrows)):
                    magDif[mm] = master[row][magr] - matchrows[mm][magr]
                    # dists[mm] = np.sqrt((master[row][xo]-matchrows[mm][xo])**2 + (master[row][yo]-matchrows[mm][yo])**2)
                    small = np.argmin(magDif)
                    master[row][xo+dd+2] = matchrows[small][id]
                row = row + 1

            else:
              master = np.delete(master, row, 0)

            if (row >= len(master)):
                nF = False
                # print(len(master))

    header =  "xr yr flux c_star magr id xc yc xo yo id2 id3 id4"
    # header =  "xr yr mag id xc yc xo yo id2 id3 id4"

    np.savetxt(workdir+catDir+"master_"+targname+"_"+filter+".txt",master,fmt=fmt,header=header)

    return None

def wcsTrans(targname,filter):

    jdanUse = getJdan(targname,filter)

    cat = np.loadtxt(workdir+catDir+"master_"+targname+"_"+filter+".txt")

    newCols = np.zeros((len(cat),2))

    imgfile = workdir+'flc_fits/'+jdanUse[0]+"_flc.fits"

    image = fits.open(imgfile)
    w = wcs.WCS(header=image[1].header,fobj=image)

    # Applied to distortion corrected values
    # Since drawing from file, the "master" is just the first one listed.
    newCols[:,0], newCols[:,1] = w.wcs_pix2world(cat[:,xc],cat[:,yc],1) #ra, dec

    image.close()

    cat = np.hstack((cat, newCols))

    # header =  "xr yr mag id xc yc xo yo id2 id3 id4 ra dec"
    header =  "xr yr flux c_star magr id xc yc xo yo id2 id3 id4 ra dec"
    np.savetxt(workdir+coordDir+targname+"_"+filter+"_coords.txt",cat,header=header,fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f %d %d %d %1.5f %1.5f")

    return None


def regMake(targname,filter):
    jdanUse = getJdan(targname,filter)

    master = np.loadtxt(workdir+catDir+"master_"+targname+"_"+filter+".txt")

    for jj in range(len(jdanUse)):
        cat = np.loadtxt(workdir+catDir+jdanUse[jj]+"_"+targname+"_oc.dat",comments='#')

        if jj==0:
            idcol = id
        else:
            idcol = xo+jj+1

        rowsMast = np.transpose(master)

        # print(rowsMast.shape)

        newIDcol = rowsMast[idcol]
        idx = np.asarray(newIDcol,int)
        #
        reg = cat[idx]

        np.savetxt(workdir+catDir+jdanUse[jj]+"_"+targname+".reg", reg[:,[xr, yr]], fmt="%1.5f")

    return None

def pullMags(targname,filter):
    jdanUse = getJdan(targname,filter)

    master = np.loadtxt(workdir+coordDir+targname+"_"+filter+"_coords.txt")

    # coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #working line

    # trying to output xr and yr
    coordRows = master[:,[ra_ind,dec_ind,flux,c_star,xr,yr]] #edited

    newCols = np.zeros((len(coordRows),4))

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

        newCols[:,jj] = reg[:,magr]

    magList = np.hstack((coordRows, newCols))

    header = 'RA DEC flux c_star xr yr mag1 mag2 mag3 mag4'

    np.savetxt(workdir+magDir+targname+"_"+filter+"_magList_xy.dat", magList, fmt="%1.5f",header=header)

    return None

#############################################################################




#############################################################################
def wrapAll(targname,filter):

    distCor(targname,filter)
    offCor(targname,filter)
    matchWJCs(targname,filter)
    wcsTrans(targname,filter)
    pullMags(targname,filter)
    # regMake(targname,filter)

    return None

##############################################
# Run everything on everything

# targnamesList = np.loadtxt("targnamesDirections.txt",dtype=str)
# filterList = ["F606W","F814W"]
#
# start=time.time()
# for tt in range(len(targnamesList)):
#     print(targnamesList[tt])
#     for ff in range(len(filterList)):
#         wrapAll(targnamesList[tt],filterList[ff])
# print('It took {0:0.1f} minutes'.format((time.time() - start)/60.))
#



#END
