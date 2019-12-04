#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Oct. 2019
	ED_Chapter4
	@author: ZYW @ BNU
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
import os
from matplotlib import font_manager as fm, rcParams
import astropy.units as u
##------------parameters settings-----------------##
pixel_sides = 10#pixels per cm

N = np.array([3,3,3])#wave node numbers
L = np.array([100,100,100])#unit:cm
A = np.array([2,12,5])#initial intensities
pi = np.pi
K_0 = np.array([N[0]*pi/L[0],N[1]*pi/L[1],N[2]*pi/L[2]])/pixel_sides#wave vector
fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
prop = fm.FontProperties(fname=fpath)

xx = np.linspace(0,L[0]*pixel_sides,L[0]*pixel_sides)
yy = np.linspace(0,L[1]*pixel_sides,L[1]*pixel_sides)
zz = np.zeros(0,L[1]*pixel_sides,L[1]*pixel_sides)

##------------functions settings-----------------##
'''
def E_x(x,y,z):
	return A[0]*np.cos(x*K_0[0])*np.sin(y*K_0[1])*np.sin(z*K_0[2])
def E_y(x,y,z):
	return A[1]*np.sin(x*K_0[0])*np.cos(y*K_0[1])*np.sin(z*K_0[2])
'''
def E_z(x,y,z):
	return A[2]*np.sin(x*K_0[0])*np.sin(y*K_0[1])*np.cos(z*K_0[2])
#Intensities of 3 directions in Cartissian coordinate
xx, yy= np.meshgrid(xx, yy)
zz = 11
E = E_z(xx,yy,zz)

def draw3D(X,Y,Z,angle):
    fig = plt.figure(figsize=(15,7))
    ax1 = fig.add_subplot(121)
    ax1.imshow(Z,cmap='YlGnBu')
    ax2 = fig.add_subplot(122,projection='3d')
    ax2.view_init(angle[0],angle[1])
    ax2.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='rainbow',alpha=0.8)
    surf = ax2.contourf(X,Y,Z,zdir='z',offset=-5,cmap='rainbow')
    ax1.set_title(r'$E_z-plane-figure$')
    ax2.set_title(r'$E_z-hologram$')
    plt.tight_layout()
    plt.savefig('ED_4.png',dpi=600)
    plt.show()

##------------data writting & figures making-----------------##

draw3D(xx,yy,E,(45,45))
exit()
