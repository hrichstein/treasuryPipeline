import numpy as np
from astropy.io import fits
from hst_func import *

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

matchtol = 1.0

for a in range(len(imlist)):

## Load image
  tempim = fits.open(workdir+imlist[a]+"_flc.fits")
  xoff = float(tempim[0].header["POSTARG1"])
  yoff = float(tempim[0].header["POSTARG2"])


## Load the respective catalog
  cat = np.loadtxt(workdir+catDir+imlist[a]+"_ERIDANUS-III_F606W.dat", comments="#")

## Apply offsets

# Create an array for the new values
  newcol = np.zeros((len(cat),2))
  newcol[:,0] = cat[:,xc] - (offsetlist[a] * xoff)
  newcol[:,1] = cat[:,yc] - (offsetlist[a] * yoff)

## Combine to single array and save out
  cat = np.hstack((cat, newcol))

  header =  "xr yr mag id xc yc xo yo"
  np.savetxt(workdir +catDir+ imlist[a] + "_offsetCor.dat", cat, fmt="%1.5f", header=header)
