#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt


# In[7]:


d6 = np.genfromtxt('hor1dir6pix/HORI_pix_2212_d6_dist.dat',names=True)


# In[4]:


psf = np.genfromtxt('elena_cats/HOROLOGIUM_CF.1.PSF.CAT',names=True)


# In[8]:


fig,ax = plt.subplots(figsize=(5,7))

ax.scatter(psf['m606c']-psf['m814c'],psf['m814c'],alpha=0.5,label='PSF')
ax.scatter(d6['mean_f606w']-d6['mean_f814w'],d6['mean_f814w'],alpha=0.5,label='AP')


ax.set_ylim(28,18)
ax.set_xlim(-1,0.5)
ax.legend()

plt.show()


# In[9]:


len(d6[d6['pos_std_f814w']<0.1])


# In[12]:


keep_814_ = d6['mean_f814w']!=d6['mean_f814w']
for ll in range(len(d6)):
    temp_keep_814_1 = np.logical_and(np.logical_and(d6['mean_f814w']>=20,d6['mean_f814w']<=24.5),
                             np.logical_and(d6['pos_std_f814w']<0.1,d6['stdev_f814w']<0.1))
    temp_keep_814_ = np.logical_and(temp_keep_814_1,d6['mean_f606w']-d6['mean_f814w']<-0.3)
    keep_814_ = np.logical_or(keep_814_,temp_keep_814_)



# In[13]:


len(d6['mean_f814w'][keep_814_])


# In[25]:


fig,ax = plt.subplots(figsize=(5,7))

ax.scatter(psf['m606c']-psf['m814c'],psf['m814c'],alpha=0.5,label='PSF')
# ax.scatter(d6['mean_f606w']-d6['mean_f814w'],d6['mean_f606w'],alpha=0.5,label='AP')
ax.scatter(d6['mean_f606w'][keep_814_]-d6['mean_f814w'][keep_814_],
           d6['mean_f814w'][keep_814_],alpha=0.5,label='keep_814_')


ax.set_ylim(28,18)
ax.set_xlim(-1,0.5)
ax.legend()

plt.show()


# In[15]:


gen_keep_814_ = d6[keep_814_]

# mean2_1 = d6['mag2_f606w'][keep_814_]-d6['mag1_f606w'][keep_814_]


# In[26]:


len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-0) <= 1e-3])


# In[27]:


len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-1) <= 1e-3])


# In[28]:


len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-2) <= 1e-3])


# In[29]:


len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-3) <= 1e-3])


# In[31]:


len(gen_keep_814_[abs(gen_keep_814_['cut_idx_f814w']-4) <= 1e-3])


# In[32]:


keep_814_er = gen_keep_814_['mean_f814w']!=gen_keep_814_['mean_f814w']
keep_814_2 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep_814_['cut_idx_f814w']-1) >= 1e-3)
keep_814_2 = np.logical_or(keep_814_er,keep_814_2)


# In[33]:


keep_814_3 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep_814_['cut_idx_f814w']-2) >= 1e-3)
keep_814_3 = np.logical_or(keep_814_er,keep_814_3)


# In[34]:


keep_814_4 = np.logical_and(abs(gen_keep_814_['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep_814_['cut_idx_f814w']-3) >= 1e-3)
keep_814_4 = np.logical_or(keep_814_er,keep_814_4)


# In[36]:


mean2_1 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_2]-gen_keep_814_['mag2_f814w'][keep_814_2])
print(mean2_1)


# In[37]:


mean3_1 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_3]-gen_keep_814_['mag3_f814w'][keep_814_3])
print(mean3_1)


# In[38]:


mean4_1 = np.mean(gen_keep_814_['mag1_f814w'][keep_814_4]-gen_keep_814_['mag4_f814w'][keep_814_4])
print(mean4_1)


# In[ ]:
