import numpy as np
import os


# Calculate median and std for the mags

directory = "/Volumes/Spare Data/Hannah_Data/mags0811/matchMag_3/"
out_dir = "/Volumes/Spare Data/Hannah_Data/magsWerrs0811/"

dirk = os.fsencode(directory)

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    outName = file.strip('.dat')

    data = np.genfromtxt(directory+filename,dtype=float)

    newCol = np.zeros((len(data),2))
    for dd in range(len(data)):
        newCol[dd,0] = np.median(data[dd][4:8])
        newCol[dd,1] = np.std(data[dd][4:8])

    data = np.hstack((data, newCol))

    header = 'RA DEC flux c_star mag1 mag2 mag3 mag4 median stdev'
    # header = 'RA DEC mag1 mag2 mag3 mag4 median stdev'

    np.savetxt(out_dir+outName+'_std.dat',data,header=header,fmt='%1.5f')



# END
