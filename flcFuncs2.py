import numpy as np
from astropy.io import fits
from hst_func import *
from astropy import wcs
import time

workdir = "/Volumes/Spare Data/Hannah_Data/"
# cupDir = "catRawMags0501/"
# inner_work = 'hor1flcs/'
cupDir = "catRawMags2804/"
catDir = "catRawMags2804/catDir/"
# catDir = "catRawMags0501/catDir/"
# coordDir = 'mags0501/coordDir/'
# posDir = '/Volumes/Spare Data/Hannah_Data/positions_d4/'
# magDir = 'mags0501/magDir/'
posDir = workdir+catDir # zeroth iteration

# out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir1803/'
out_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
# posDir = out_dir # first iteration after 6D transform

xr, yr, flux, c_star, magr = 0, 1, 2, 3, 4

id, xc, yc, xt, yt, id2, id3, id4 = 5,6,7,8,9,10,11,12

# first iteration
# id, xc, yc, xo, yo, id2, id3, id4 = 5,6,7,8,9,10,11,12

ra_ind, dec_ind = 13,14

# fmt = "%1.5f %1.5f %1.5f %1.4 %1.5f %1.5f %1.5f %1.5f %d %d %d"
fmt = "%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f %d %d %d"

matchtol = 5.0 #20 pixels arcsec

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
        cat = np.loadtxt(workdir+cupDir + jdanUse[ff]+'_'+targname+'_'+filter+'_wMag.dat')

        #Do correction
        cor = acsDistortion(workdir+'wfc_'+filter,cat[:,xr],cat[:,yr])

        #Add columns
        cat = np.hstack((cat,cor))

        header = 'xr yr flux c_star magr id xc yc'

        np.savetxt(workdir+catDir+jdanUse[ff]+'_'+targname+'_'+filter+'_dc.dat',cat,fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f",header=header)

    return None

# Offset correction
# Replaced by Paul's transformation code
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
        np.savetxt(workdir+catDir+ jdanUse[ff] + "_"+targname+"_"+filter+"_oc.dat", cat, fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f", header=header)

    return None
# Matching time
def addTranscols(targname,filter):

    jdanUse = getJdan(targname,filter)

    for ff in range(len(jdanUse)):

        cat = np.loadtxt(workdir+catDir+jdanUse[ff]+"_"+targname+"_"+filter+"_dc.dat")

        # transCat = np.loadtxt(posDir+ jdanUse[ff] +"_"+targname+'_'+ filter +"_t.dat")

        transCat = np.loadtxt('/Volumes/Spare Data/Hannah_Data/hor1dir2804/'+ jdanUse[ff] +"_"+targname+'_'+ filter +"_t.dat")


        newCol = np.zeros((len(cat),2))

        newCol[:,0] = transCat[:,0]
        newCol[:,1] = transCat[:,1]

        cat = np.hstack((cat, newCol))

        header =  "xr yr flux c_star magr id xc yc xt yt"

        np.savetxt("hor1dir2804/"+jdanUse[ff] + "_"+targname+"_"+filter+"_at.dat", cat, fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f", header=header)

        # np.savetxt(out_dir+"dir2403/"+jdanUse[ff] + "_"+targname+"_"+filter+"_at.dat", cat, fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f", header=header)

    return None

def matchWJCs(targname,filter,matchtol=matchtol):

    jdanUse = getJdan(targname,filter)

    # master = np.loadtxt(posDir+ jdanUse[0] +"_"+targname+'_'+ filter +"_dc_t.dat")

    # For zeroeth iteration
    # master = np.loadtxt(posDir+ jdanUse[0] +"_"+targname+'_'+ filter +"_oc.dat")

    # For every other iteration
    master = np.loadtxt(out_dir+jdanUse[0] +"_"+targname+'_'+ filter +"_at.dat")

    # master = np.loadtxt(posDir+jdanUse[0] +"_"+targname+'_'+ filter +"_atnC.dat")

    # Create an array of zeros with columns equal to the number of non-master dithers to store the matching id for each source

    matchids = np.zeros((len(master), (len(jdanUse)-1)))

    master = np.hstack((master, matchids))

    # Loop through other images

    for dd in range(len(jdanUse)-1):

        # Load catalogs

        # cat = np.loadtxt(posDir+ jdanUse[dd+1] +"_"+targname+'_'+ filter +"_dc_t.dat")

        # For zeroth iteration
        # cat = np.loadtxt(posDir + jdanUse[dd+1] +"_"+targname+'_'+ filter +"_oc.dat")
        # outname = "master_"+targname+"_"+filter+".txt"

        # For after first iteration
        cat = np.loadtxt(out_dir+jdanUse[dd+1] +"_"+targname+'_'+ filter +"_at.dat")
        outname = "master_"+targname+"_"+filter+".txt"

        # cat = np.loadtxt(posDir+jdanUse[dd+1] +"_"+targname+'_'+ filter +"_atnC.dat")

        nF = True
        row = 0

        while (nF): #notFinished

            matchrows = cat[(abs(master[row][xt] - cat[:,xt]) <= matchtol) & (abs(master[row][yt] - cat[:,yt]) <= matchtol)]

            # Setting the proper column number to the matching index.
            if (len(matchrows) == 1):
              master[row][xt+dd+2] = matchrows[0][id]
              row = row + 1

            elif (len(matchrows) > 1):
                # print("more than one source")
                # print(len(matchrows))

                magDif = np.zeros((len(matchrows),1))
                for mm in range(len(matchrows)):
                    magDif[mm] = master[row][magr] - matchrows[mm][magr]
                    # dists[mm] = np.sqrt((master[row][xo]-matchrows[mm][xo])**2 + (master[row][yo]-matchrows[mm][yo])**2)
                    small = np.argmin(magDif)
                    master[row][xt+dd+2] = matchrows[small][id]
                row = row + 1

            else:
              master = np.delete(master, row, 0)

            if (row >= len(master)):
                nF = False
                # print(len(master))

    header =  "xr yr flux c_star magr id xc yc xt yt id2 id3 id4"
    # header =  "xr yr mag id xc yc xo yo id2 id3 id4"

    # np.savetxt(out_dir+"dir2403/master_"+targname+"_"+filter+".txt",master,fmt=fmt,header=header)

    np.savetxt(out_dir+outname,master,fmt=fmt,header=header)

    return None

def wcsTrans(targname,filter):

    jdanUse = getJdan(targname,filter)

    # cat = np.loadtxt(out_dir+"dir2403/master_"+targname+"_"+filter+".txt")
    # For zeroth iteration
    # cat = np.loadtxt(out_dir+"master_"+targname+"_"+filter+".txt")

    # For afterwards iteration
    cat = np.loadtxt(out_dir+"master_"+targname+"_"+filter+".txt")

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
    header =  "xr yr flux c_star magr id xc yc xt yt id2 id3 id4 ra dec"
    # np.savetxt(out_dir+"dir2403/"+targname+"_"+filter+"_coords.txt",cat,header=header,fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f %d %d %d %1.5f %1.5f")

    np.savetxt(out_dir+targname+"_"+filter+"_coords.txt",cat,header=header,fmt="%1.5f %1.5f %1.5f %1.4f %1.5f %d %1.5f %1.5f %1.5f %1.5f %d %d %d %1.5f %1.5f")

    return None


# def regMake(targname,filter):
#     jdanUse = getJdan(targname,filter)
#
#     master = np.loadtxt(workdir+catDir+"master_"+targname+"_"+filter+".txt")
#
#     for jj in range(len(jdanUse)):
#         cat = np.loadtxt(workdir+catDir+jdanUse[jj]+"_"+targname+"_oc.dat",comments='#')
#
#         if jj==0:
#             idcol = id
#         else:
#             idcol = xo+jj+1
#
#         rowsMast = np.transpose(master)
#
#         # print(rowsMast.shape)
#
#         newIDcol = rowsMast[idcol]
#         idx = np.asarray(newIDcol,int)
#         #
#         reg = cat[idx]
#
#         np.savetxt(workdir+catDir+jdanUse[jj]+"_"+targname+".reg", reg[:,[xr, yr]], fmt="%1.5f")
#
#     return None

def pullMags(targname,filter):
    jdanUse = getJdan(targname,filter)

    # master = np.loadtxt(out_dir+"dir2403/"+targname+"_"+filter+"_coords.txt")

    master = np.loadtxt(out_dir+targname+"_"+filter+"_coords.txt")

    # coordRows = master[:,[ra_ind,dec_ind,flux,c_star]] #working line

    # trying to output xr and yr
    coordRows = master[:,[ra_ind,dec_ind,flux,c_star,xr,yr,xc,yc,xt,yt]] #edited

    newCols = np.zeros((len(coordRows),4))

    for jj in range(len(jdanUse)):
        # cat = np.loadtxt(posDir+ jdanUse[jj] +"_"+targname+'_'+ filter +"_dc_t.dat",comments='#')

        # Zero iteration
        cat = np.loadtxt(posDir+ jdanUse[jj] +"_"+targname+'_'+ filter +"_oc.dat",comments='#')

        # First iteration
        # cat = np.loadtxt(out_dir+"dir2403/"+ jdanUse[jj] +"_"+targname+'_'+ filter +"_at.dat",comments='#')

        # cat = np.loadtxt(out_dir+jdanUse[jj] +"_"+targname+'_'+ filter +"_atnC.dat",comments='#')

        if jj==0:
            idcol = id
        else:
            idcol = xt+jj+1

        rowsMast = np.transpose(master)

        newIDcol = rowsMast[idcol]
        idx = np.asarray(newIDcol,int)
        #
        reg = cat[idx]

        newCols[:,jj] = reg[:,magr]

    magList = np.hstack((coordRows, newCols))

    header = 'RA DEC flux c_star xr yr xc yc xt yt mag1 mag2 mag3 mag4'

    # np.savetxt(out_dir+"dir2403/"+targname+"_"+filter+"_magList_xy.dat", magList, fmt="%1.5f",header=header)

    np.savetxt(out_dir+targname+"_"+filter+"_magList_xy.dat", magList, fmt="%1.5f",header=header)

    return None

#############################################################################



#############################################################################
def wrapAll(targname,filter):

    # distCor(targname,filter)
    # offCor(targname,filter)
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
