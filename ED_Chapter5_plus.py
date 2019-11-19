#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
	'''
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager as fm, rcParams
import shutil

delList = []
delDir = './figures'
delList = os.listdir(delDir )

for f in delList:
    filePath = os.path.join( delDir, f )
    if os.path.isfile(filePath):
        os.remove(filePath)
    elif os.path.isdir(filePath):
    	shutil.rmtree(filePath,True)


##------------parameters settings-----------------##
E_file = './E_map.dat'
E_0 = np.loadtxt(E_file)

c = 1#speed of light
eps = 1#vaccum dielectirc number
pi = np.pi
l = 300#wave length
k= 2*pi/l#wave number
P_tt = 1000#acceleration of electic dipole
pixels = E_0.shape[0]#resolution of the map
perc_2 = 4*pi*eps*c**3
total_T = 3
omega = 0.05

##------------matrix settings-----------------##

E = np.zeros(shape=(pixels,pixels,total_T),dtype='float')# electric field intensity
B = np.zeros(shape=(pixels,pixels,total_T),dtype='float')# magnetic field intensity
R = np.zeros(shape=(pixels,pixels),dtype='float')#radius or the distance from the map centre
N = np.logspace(-0.9,-0.3,3)#contours label numbers
L = np.zeros(pixels,dtype='float')#any axes of x or y
phi = np.zeros(total_T,dtype='float')


##---------------computing--------------------##
for m in range(total_T):
	phi[m] = -1*omega*m
	E[:,:,m] = (E_0[:,:]*exp(phi[m])).real

##------------data writting & figures making-----------------##

fig, ax = plt.subplots()
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
prop = fm.FontProperties(fname=fpath)


for m in range(total_T):
	plt.contour(abs(E[:,:,m]),N,linewidth=0.01,cmap = 'rainbow')
	#plt.clabel(a,fontsize=5)
	plt.imshow(E[:,:,m],cmap='YlGnBu',vmin=-1,vmax=1)
	plt.axis('off')
	plt.savefig('./figures/fig%d.png'%(m+1),size=(19.2,10.8),dpi=600)
	plt.clf()


exit()