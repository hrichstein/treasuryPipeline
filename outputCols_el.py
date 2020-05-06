import numpy as np

main_dir = '/Volumes/Spare Data/Hannah_Data/hor1dir2804/'
file = 'zpt_flcs_0605.dat'

data = np.genfromtxt(main_dir+file,names=True)

newCol = np.zeros((len(data),22))

newCol[:,0] = data['RA_f606w']
newCol[:,1] = data['DEC_f606w']
newCol[:,2] = data['flux_f606w']
newCol[:,3] = data['c_star_f606w']
newCol[:,4] = data['xt_1_f606w']
newCol[:,5] = data['yt_1_f606w']
newCol[:,6] = data['mean_f606w']
newCol[:,7] = data['magZPT_f606w']
newCol[:,8] = data['stdev_f606w']
newCol[:,9] = data['errZPT_f606w']
newCol[:,10] = data['pos_std_f606w']

newCol[:,11] = data['RA_f814w']
newCol[:,12] = data['DEC_f814w']
newCol[:,13] = data['flux_f814w']
newCol[:,14] = data['c_star_f814w']
newCol[:,15] = data['xt_1_f814w']
newCol[:,16] = data['yt_1_f814w']
newCol[:,17] = data['mean_f814w']
newCol[:,18] = data['magZPT_f814w']
newCol[:,19] = data['stdev_f814w']
newCol[:,20] = data['errZPT_f814w']
newCol[:,21] = data['pos_std_f814w']

header = 'RA_f606w DEC_f606w flux_f606w c_star_f606w x_f606w y_f606w rawMean_f606w zptMean_f606w rawErr_f606w zptErr_f606w  pos_std_f606w RA_f814w DEC_f814w flux_f814w c_star_f814w x_f814w y_f814w rawMean_f814w zptMean_f814w rawErr_f814w zptErr_f814w  pos_std_f814w'

np.savetxt(main_dir+'HORI_comb0605.dat',newCol,fmt='%1.5f',header=header)











# End
