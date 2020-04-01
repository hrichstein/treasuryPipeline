import numpy as np
import time
from flcFuncs import getJdan

workdir = "/Volumes/Spare Data/Hannah_Data/"
catDir = "matchForm/catDir/"
coordDir = 'matchForm/coordDir/'

def stackMags(targname,filter):
    jdanUse = getJdan(targname,filter)

    cat1 = np.loadtxt(workdir+catDir+jdanUse[0]+"_"+targname+"_magList.dat",dtype=float)
    cat2 = np.loadtxt(workdir+catDir+jdanUse[1]+"_"+targname+"_magList.dat",dtype=float)
    cat3 = np.loadtxt(workdir+catDir+jdanUse[2]+"_"+targname+"_magList.dat",dtype=float)
    cat4 = np.loadtxt(workdir+catDir+jdanUse[3]+"_"+targname+"_magList.dat",dtype=float)

    final_cat = np.array((cat1,cat2,cat3,cat4))

    # print(final_cat.shape)

    np.savetxt(workdir+catDir+targname+"_"+filter+"_magList.dat", final_cat.T, fmt="%1.5f")

    return None

targnamesList = np.loadtxt("targnamesDirections.txt",dtype=str)
filterList = ["F606W","F814W"]
#
start=time.time()
for tt in range(len(targnamesList)):
    print(targnamesList[tt])
    for ff in range(len(filterList)):
        stackMags(targnamesList[tt],filterList[ff])
print('It took {0:0.1f} seconds'.format(time.time() - start))
