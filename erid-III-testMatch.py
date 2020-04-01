import numpy as np
from astropy.io import fits
from hst_func import *
import time

start=time.time()

workdir = "/Volumes/Spare Data/Hannah_Data/"
catDir = "matchForm/catDir/"

# Create list of images to be corrected
imlist = ["jdan03dpq","jdan03drq","jdan03dyq","jdan03e3q"]

# Create corresponding list of filters (and offsets) to be applied to each image
filterlist = ["F606W", "F606W", "F606W", "F606W"]

offsetlist = [20.0, 20.0, 20.0, 20.0] # This is in pixels/arcsec for ACS


# Set indice ids to be used (xc, yc, xo, yo, id1 will all be created during this script)
xr, yr, mag, id, xc, yc, xo, yo, id1 = 0, 1, 2, 3, 4, 5, 6, 7, 8


# Set the pixel tolerance for matching sources together

matchtol = 20.0

master = np.loadtxt(workdir +catDir+ imlist[0] + "_offsetCor.dat", comments="#")

# Create an array of zeros with columns equal to the number of dithers past
# the master to store the matching id for each source

matchids = np.zeros((len(master), (len(imlist)-1)))
master = np.hstack((master, matchids))


# Loop through all listed images
for a in range(len(imlist)-1):

# Load the catalog
  cat = np.loadtxt(workdir +catDir+ imlist[a+1] + "_offsetCor.dat", comments="#")

  # print(workdir +catDir+ imlist[a+1])
# Loop through every source in the master list and check for matches
# in the particular image (use a while loop for this)

  notfinished = True
  row = 0

  while (notfinished):

# Check to see how many sources match a given master source within tolerance
    matchrows = cat[(abs(master[row][xo] - cat[:,xo]) < matchtol) & \
                    (abs(master[row][yo] - cat[:,yo]) < matchtol)]

# If only one source matches, store the corresponding id
# and iterate the row variable one
    if (len(matchrows == 1)):
      master[row][xo+a+1] = matchrows[0][id]
      row = row + 1

# If it has either zero or more than one match, delete it from the master list
# This assumes a relatively sparse field and would need to be reconsidered
# for a denser region

    else:
      master = np.delete(master, row, 0)
      # print(len(master))
    if (row >= len(master)):
      notfinished = False
      print(len(master))


####
   # Save out the master file and create region files for all image files of
   # the matched sources for visual inspection
####

header =  "xr yr mag id xc yc xo yo id2 id3 id4"

np.savetxt(workdir+catDir+"master_eridIII.txt", master, fmt="%1.5f", header=header)

for a in range(len(imlist)):

# Load the specific catalog
  cat = np.loadtxt(workdir +catDir+ imlist[a] + "_offsetCor.dat", comments="#")

# Create a list of integers using the ids from the master catalog
# (Definitely a better way to do this, but it gets the job done)
  selectids = []

# Set the column to reference
  if (a == 0):
    idcol = id
  else:
    idcol = xo + a

# Loop through the master list and convert floats to integers
  for b in range(len(master)):
    selectids.append(int(master[b][idcol]))

# Create a subselection of each image's catalog based on the master
  reg = cat[selectids]

# Save out to a region file, only keeping the raw image positions
  np.savetxt(workdir+catDir+imlist[a]+"_test.reg", reg[:,[xr, yr]], fmt="%1.5f")


print('It took {0:0.1f} seconds'.format(time.time() - start))
