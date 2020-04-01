import numpy as np

dir = '/Users/hr8jz/Box Sync/Research/source_lists/june13/'

def countLines(filename):
    data = np.genfromtxt(filename,usecols=0)

    return len(data)


namefile='origListNamesforCounts.txt'
names=np.genfromtxt(namefile,dtype=str)

# counts = np.zeros(len(names),dtype=int)
fileOut = open('origCounts.txt','w')
for ff in range(len(names)):
    prName = names[ff].strip('_sfErr.dat')
    counts = countLines(dir+names[ff])

    fileOut.write('{0} {1:d} \n'.format(prName,counts))

fileOut.close()
