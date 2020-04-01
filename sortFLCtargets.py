import numpy as np

#generates files containing which flcs belong to which target

file = 'targnamesDirections.txt'
tgn = np.genfromtxt(file,dtype=str)

def listMake(targname,file1):
    data = np.genfromtxt(file1,dtype=str)

    targs = data[:,1]
    flcs = data[:,0]
    filt1 = data[:,2]
    filt2 = data[:,3]


    tmpFile = open(targname+'_flcs.txt','w')

    for tt in range(len(targs)):
        if targs[tt]==targname:
            if (filt1[tt]=='F606W') or (filt2[tt]=='F606W'):
                filt_txt = 'F606W'
            else:
                filt_txt = 'F814W'

            tmpFile.write(flcs[tt].strip('_WJC.fits') + ' ' + filt_txt + '\n')

    tmpFile.close()

    return None

for nn in range(len(tgn)):
    listMake(tgn[nn],'sortedFLCs.dat')
    # listMake(tgn[nn],'sortTriEast.dat')
