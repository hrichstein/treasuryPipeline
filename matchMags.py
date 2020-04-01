import numpy as np
import time


start=time.time()
idxDir = '/Volumes/Spare Data/Hannah_Data/sp_match0811_3/'
magDir = '/Volumes/Spare Data/Hannah_Data/mags0811/magDir/'
finalDir = '/Volumes/Spare Data/Hannah_Data/mags0811/matchMag_3/'

targnames = np.genfromtxt('targnamesDirections.txt',dtype=str)
# targnames=['BOOTES-II-NORTH','BOOTES-II-SOUTH','CARINA','DRACO-II']

filters = ['F606W','F814W']

fileOut = open('newCounts.txt','w')
for tt in range(len(targnames)):
    for ff in range(len(filters)):
        dataFile = np.genfromtxt(magDir+targnames[tt]+"_"+filters[ff]+"_magList.dat")
        idxFile = np.genfromtxt(idxDir+targnames[tt]+"_"+filters[ff]+"_match.txt",dtype=int)

        outArr = dataFile[idxFile]

        header = 'RA DEC flux c_star mag1 mag2 mag3 mag4'

        np.savetxt(finalDir+targnames[tt]+'_'+filters[ff]+'.dat',outArr,fmt='%1.5f')

    counts=len(outArr)
    fileOut.write('{0} {1:d} \n'.format(targnames[tt],counts))

fileOut.close()
print('It took {0:0.1f} seconds'.format(time.time() - start))
