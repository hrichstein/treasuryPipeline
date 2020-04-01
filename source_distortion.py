import numpy as np
from astropy.io import fits
from hst_func import *
from astropy import wcs

mainDir = "/Volumes/Spare Data/Hannah_Data/"
workdir = "/Volumes/Spare Data/Hannah_Data/matchForm/"

catDir = 'catDir/'
coordDir = 'coordDir/'

# have a wrapper go through the targname list, extract the jdan combo and filter
xr, yr, mag, id, xc, yc, ra, dec, id1 = 0, 1, 2, 3, 4, 5, 6, 7, 8

matchtol = 1.0

offset = 20.0 #pixels/arcsec

# create a function to take these pieces of info  and perform the distortion corretion.
# looks like the fits file is only used to get the POSTARG1 and POSTARG2 values -> use the sortFLCs to extract and keep these keyword values on file
def distCor(jdan,targname,filter):

    jdan = jdan.strip('_WJC.fits')
    #Load catalog
    cat = np.loadtxt(workdir+jdan+'_'+targname+'_'+filter+'_mF.dat')

    #Do correction
    cor = acsDistortion(mainDir+'wfc_'+filter,cat[:,xr],cat[:,yr])

    #Add columns
    cat = np.hstack((cat,cor))

    header = '# xr yr mag id xc yc'

    np.savetxt(workdir+catDir+jdan+'_'+targname+'_'+filter+'.dat',cat,fmt="%1.5f",header=header)

    return None

def wcsTrans(jdan,targname,filter):

    flcName = jdan.replace("WJC.fits","flc.fits")

    jdan = jdan.strip('_WJC.fits')

    cat = np.loadtxt(workdir+catDir+jdan+'_'+targname+'_'+filter+'.dat')

    newCols = np.zeros((len(cat),2))

    # flcName = jdan.replace("WJC.fits","flc.fits")
    imgfile = mainDir+flcName

    image = fits.open(imgfile)
    w = wcs.WCS(header=image[1].header,fobj=image)

    newCols[:,0], newCols[:,1] = w.wcs_pix2world(cat[:,xc],cat[:,yc],1) #ra, dec

    image.close()

    cat = np.hstack((cat, newCols))

    header =  "xr yr mag id xc yc ra dec"

    jdan = flcName.strip('_flc.fits')

    np.savetxt(workdir+coordDir+jdan+'_'+targname+'_'+filter+'.dat',cat,header=header,fmt="%1.5f %1.5f %1.5f %d %1.5f %1.5f %1.5f %1.5f ")

    return None


def matchFunc(targname,filter='F606W'):
    # take in txt file with list of sortFLCs
    # generate the coordinate files to call
    # read in the RAs and decs

    filename = targname+'_flcs.txt'

    data = np.genfromtxt(filename,dtype='<U30')

    flcNames = data[:,0]
    filts = data[:,1]

    coordFiles = []

    for ff in range(len(flcNames)):
        if filts[ff]==filter:
            coordFiles.append(flcNames[ff])

    coordFiles = np.array(coordFiles,dtype='<U50')

    jdanNames = np.copy(coordFiles)

    for aa in range(len(coordFiles)):
        tmp = str(coordFiles[aa]).strip('WJC.fits') #leaving the _ in
        jdanNames[aa] = tmp+targname+'_'+filter+'.dat'

    # master = np.genfromtxt(workdir+coordDir+jdanNames[0],names=True)
    master = np.genfromtxt(workdir+coordDir+jdanNames[0],comments='#')

    matchids = np.zeros((len(master), (len(jdanNames)-1)))
    #
    # mastID = np.arange(0,len(master),1)
    #
    # # mastID = np.column_stack((mastID, matchids))
    # print(master.shape)
    # print(matchids.shape)
    master = np.concatenate((master, matchids),axis=1)
    #
    # ra1 = master[ra]
    # dec1 = master[dec]

    for dd in range(len(jdanNames)-1):
        cat = np.genfromtxt(workdir+coordDir+jdanNames[dd+1],names=True)

        ra2 = cat['ra']
        dec2 = cat['dec']

        nF = True #not finished
        row = 0
        counter = 0

        while (nF):
            ra1 = master[row][ra]
            dec1 = master[row][dec]

            tmp_gcds = np.zeros(len(cat))
            for gg in range(len(cat)):
                tmp_gcds[gg] = get_gcd(ra1,dec1,ra2[gg],dec2[gg])

            mindx = np.argmin(tmp_gcds)

            matchrows = cat[(tmp_gcds/3600.) <= 1]

            if len(matchrows) == 1:
                master[row][ra+dd+1] = matchrows[0][id]
                row=row+1

            elif len(matchrows) > 1:
                master[row][ra+dd+1] = cat[mindx][id]
                row=row+1

            else:
                master = np.delete(master, row, 0)

            if (row >= len(master)):
                nF = False
                print('1 Run Done')

            counter+=1

            if counter%50==0:
                print(counter)

    header =  "xr yr mag id xc yc ra dec id1 id2 id3"

    np.savetxt(workdir+coordDir+"test.txt", master, fmt="%1.5f", header=header)

    return None

    #If I use spherematch, I can only compare two at a time. Compare each dither to the master. Get matching indices.
    #Or try to do run Paul's matching code, except using gcd instead of pixel distance. would get one list containing the matching ids



# def ditherOff(jdan,targname,filter):
#
#     cat = np.loadtxt(workdir+catDir+jdan+'_'+targname+'_'+filter+'.dat')
#
#     flcName = jdan.replace("WJC.fits","flc.fits")
#
#     tempim = fits.open(maindir+flcName)
#     xoff = float(tempim[0].header["POSTARG1"])
#     yoff = float(tempim[0].header["POSTARG2"])
#
#
#     newCols = np.zeros((len(cat),2))
#
#     newCols[:,0] = cat[:,xc] - (offsetlist * xoff)
#     newCols[:,1] = cat[:,yc] - (offsetlist * yoff)
#
#     cat = np.hstack((cat, newcol))
#
#     jdan = flcName.strip('_flc.fits')
#
#     header =  "xr yr mag id xc yc xo yo"
#
#     np.savetxt(workdir+offDir+jdan+'_'+targname+'_'+filter+'.dat')
#
#     return None





#END
