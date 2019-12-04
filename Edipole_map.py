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
from mpl_toolkits.mplot3d import Axes3D
import easyraid.easyraid as erd#a script call easyraid

##------------parameters settings-----------------##

l = 100#wave length
P_tt = 1000#acceleration of electic dipole
pixels = 1024#resolution of the map
##------------matrix settings-----------------##

# E = np.zeros(shape=(pixels,pixels),dtype='float')#complex electric field intensity
# B = np.zeros(shape=(pixels,pixels),dtype='float')#complex magnetic field intensity
N = np.logspace(-0.9,-0.3,3)#contours label numbers
ell = np.linspace(-1*pixels//2,pixels//2,pixels)
##---------------computing--------------------##

E = erd.E2E(l=l,P_tt=P_tt,pixels=pixels)
np.savetxt('E.dat',E)




##------------data writting & figures making-----------------##



xx = np.linspace(-pixels//2,pixels//2,pixels)
yy = np.linspace(-pixels//2,pixels//2,pixels)
x,y = np.meshgrid(xx,yy)

def draw3D(X,Y,Z,angle):
    fig = plt.figure()
    ax1 = fig.add_subplot(111,projection='3d')
    ax1.view_init(angle[0],angle[1])
    ax1.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='rainbow',alpha=0.8)
    surf = ax1.contourf(X,Y,Z,zdir='z',offset=-5,cmap='rainbow')
    ax1.set_title(r'$E_z \ hologram$')
    # plt.tight_layout()
    plt.savefig('e2_3D.png',dpi=600)
    plt.show()

draw3D(xx,yy,E,(45,45))




fig= plt.figure()
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")

prop = fm.FontProperties(fname=fpath)


ax1 = plt.axes([0.05,0.52,0.4,0.4])
ax1.imshow(E,cmap='YlGnBu',vmin=-1,vmax=1)
ax1.axis('off')
ax1.set_title('E field of a dipole radiation', fontproperties=prop,fontsize=15)


ax2 = plt.axes([0.55,0.52,0.4,0.4])
ax2.imshow(E,cmap='afmhot',vmin=-1,vmax=1)
ax2.axis('off')
a = plt.contour(abs(E),N,linewidths=0.3,cmap = 'rainbow')
plt.clabel(a,fontsize=5)
ax2.set_title('E field and its contours', fontproperties=prop,fontsize=15)



ax3 = plt.axes([0.1,0.05,0.8,0.4])
ax3.plot(ell,E[pixels//2+10,:])
ax3.set_title('E field intensity in radiation direction', fontproperties=prop,fontsize=15)
ax3.grid(True)

plt.savefig('dipole_radiation.png',dpi=600)
plt.show()


exit()