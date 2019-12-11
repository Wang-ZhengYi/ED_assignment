#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pixels = 1024
c = 10
l = 75
k = 2*np.pi/l
v = 10
t_1 = 50
start = 300
A_0 = 1
d = int(l*v/c)

A = np.zeros(shape=(pixels,pixels),dtype='float')

R = np.zeros(shape=(pixels,pixels),dtype='float')

T = np.linspace(0,20,100)

def shock(A_0,l,c,T,pixels):
	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
	A = np.zeros(shape=(pixels,pixels),dtype='float')
	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
	x,y = np.meshgrid(xx,yy)
	k = 2*np.pi/l
	omega = k*c
	r = abs(x-v*T+1.0j*y)
	A = A_0*np.cos((k*(1+v*x/c/r)*r-omega*(T-r/c)))*x/r/(0.01*r+1)**2
	return A



xx = np.linspace(-1*pixels//2,pixels//2,pixels)
yy = np.linspace(-1*pixels//2,pixels//2,pixels)
x,y = np.meshgrid(xx,yy)


A = shock(A_0,l,c,10,pixels)


# plt.imshow(A0,cmap='YlGnBu',vmax=1,vmin=-1)
fig = plt.figure()
ax = fig.add_subplot(111,
	projection='3d'
	)
ax.view_init(65,45)
ax.set_zlim(-1, 1)
ax.plot_surface(x, y, A, rstride=1, cstride=1,cmap='gist_heat')
# ax.imshow(A,cmap='gist_heat',vmax=1,vmin=-1)
plt.savefig('shock.png',dpi=600)
# plt.show()
exit()

	






