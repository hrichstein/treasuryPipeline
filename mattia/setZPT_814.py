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


keep = d6['mean_f814w']!=d6['mean_f814w']
for ll in range(len(d6)):
    temp_keep1 = np.logical_and(np.logical_and(d6['mean_f814w']>=20,d6['mean_f814w']<=24.5),
                             np.logical_and(d6['pos_std_f814w']<0.1,d6['stdev_f814w']<0.1))
    temp_keep = np.logical_and(temp_keep1,d6['mean_f606w']-d6['mean_f814w']<-0.3)
    keep = np.logical_or(keep,temp_keep)



# In[13]:


len(d6['mean_f814w'][keep])


# In[25]:


fig,ax = plt.subplots(figsize=(5,7))

ax.scatter(psf['m606c']-psf['m814c'],psf['m814c'],alpha=0.5,label='PSF')
# ax.scatter(d6['mean_f606w']-d6['mean_f814w'],d6['mean_f606w'],alpha=0.5,label='AP')
ax.scatter(d6['mean_f606w'][keep]-d6['mean_f814w'][keep],
           d6['mean_f814w'][keep],alpha=0.5,label='keep')


ax.set_ylim(28,18)
ax.set_xlim(-1,0.5)
ax.legend()

plt.show()


# In[15]:


gen_keep = d6[keep]

# mean2_1 = d6['mag2_f606w'][keep]-d6['mag1_f606w'][keep]


# In[26]:


len(gen_keep[abs(gen_keep['cut_idx_f814w']-0) <= 1e-3])


# In[27]:


len(gen_keep[abs(gen_keep['cut_idx_f814w']-1) <= 1e-3])


# In[28]:


len(gen_keep[abs(gen_keep['cut_idx_f814w']-2) <= 1e-3])


# In[29]:


len(gen_keep[abs(gen_keep['cut_idx_f814w']-3) <= 1e-3])


# In[31]:


len(gen_keep[abs(gen_keep['cut_idx_f814w']-4) <= 1e-3])


# In[32]:


keeper = gen_keep['mean_f814w']!=gen_keep['mean_f814w']
keep_2 = np.logical_and(abs(gen_keep['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep['cut_idx_f814w']-1) >= 1e-3)
keep2 = np.logical_or(keeper,keep_2)


# In[33]:


keep_3 = np.logical_and(abs(gen_keep['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep['cut_idx_f814w']-2) >= 1e-3)
keep3 = np.logical_or(keeper,keep_3)


# In[34]:


keep_4 = np.logical_and(abs(gen_keep['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep['cut_idx_f814w']-3) >= 1e-3)
keep4 = np.logical_or(keeper,keep_4)


# In[35]:


keep_a = np.logical_and(abs(gen_keep['cut_idx_f814w']-0) >= 1e-3,
                       abs(gen_keep['cut_idx_f814w']-4) >= 1e-3)
keepa = np.logical_or(keeper,keep_a)


# In[36]:


mean2_1 = np.mean(gen_keep['mag1_f814w'][keep2]-gen_keep['mag2_f814w'][keep2])
print(mean2_1)


# In[37]:


mean3_1 = np.mean(gen_keep['mag1_f814w'][keep3]-gen_keep['mag3_f814w'][keep3])
print(mean3_1)


# In[38]:


mean4_1 = np.mean(gen_keep['mag1_f814w'][keep4]-gen_keep['mag4_f814w'][keep4])
print(mean4_1)


# In[ ]:
