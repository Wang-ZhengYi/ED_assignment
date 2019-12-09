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
# c = 10
# l = 75
# k = 2*np.pi/l
# v = 20
# t_1 = 50
# start = 300
# d = int(l*v/c)

# A = np.zeros(shape=(pixels,pixels),dtype='float')
# A0 = np.zeros(shape=(pixels,pixels),dtype='float')
# A1 = np.zeros(shape=(pixels,pixels),dtype='float')
# A2 = np.zeros(shape=(pixels,pixels),dtype='float')
# A3 = np.zeros(shape=(pixels,pixels),dtype='float')
# A4 = np.zeros(shape=(pixels,pixels),dtype='float')
# A5 = np.zeros(shape=(pixels,pixels),dtype='float')
# R = np.zeros(shape=(pixels,pixels),dtype='float')

# def A_z(d,pixels,k):
# 	xx = np.linspace(-1*pixels//2,pixels//2,pixels)
# 	yy = np.linspace(-1*pixels//2,pixels//2,pixels)
# 	x,y = np.meshgrid(xx,yy)
# 	# R1 = abs(x-d+pixels//2+1.0j*y)
# 	# R2 = abs(x-d*2+pixels//2+1.0j*y)
# 	# R3 = abs(x-d*3+pixels//2+1.0j*y)
# 	# R4 = abs(x-d*4+pixels//2+1.0j*y)
# 	# R5 = abs(x-d*5+pixels//2+1.0j*y)
# 	R = abs(x+1.0j*y)	
# 	return np.cos(k*R),R

xx = np.linspace(-1*pixels//2,pixels//2,pixels)
yy = np.linspace(-1*pixels//2,pixels//2,pixels)
x,y = np.meshgrid(xx,yy)


# A,R = A_z(d,pixels,k)

# for i in range(pixels):
# 	for j in range(pixels):
# 		if R[i,j] <=l:
# 			A1[i,j] = A[i,j]
# 		else:
# 			A1 = A1

# for i in range(pixels):
# 	for j in range(pixels):
# 		if R[i,j] <=2*l:
# 			A2[i,j] = A[i,j]
# 		else:
# 			A2 = A2

# for i in range(pixels):
# 	for j in range(pixels):
# 		if R[i,j] <=3*l:
# 			A3[i,j] = A[i,j]
# 		else:
# 			A3 = A3

# for i in range(pixels):
# 	for j in range(pixels):
# 		if R[i,j] <=4*l:
# 			A4[i,j] = A[i,j]
# 		else:
# 			A4 = A4
# for i in range(pixels):
# 	for j in range(pixels):
# 		if R[i,j] <=5*l:
# 			A5[i,j] = A[i,j]
# 		else:
# 			A5 = A5


# A0[:,0:start+5*l] = A5[:,pixels//2-start:pixels//2+5*l]
# A0[:,start-4*l+d:start+4*l+d] = A0[:,start-4*l+d:start+4*l+d] + A4[:,pixels//2-4*l:pixels//2+4*l]
# A0[:,start-3*l+2*d:start+3*l+2*d] = A0[:,start-3*l+2*d:start+3*l+2*d] + A3[:,pixels//2-3*l:pixels//2+3*l]
# A0[:,start-2*l+3*d:start+2*l+3*d] = A0[:,start-2*l+3*d:start+2*l+3*d] + A2[:,pixels//2-2*l:pixels//2+2*l]
# A0[:,start-l+4*d:start+l+4*d] = A0[:,start-l+4*d:start+l+4*d] + A1[:,pixels//2-l:pixels//2+l]

# np.savetxt('A0.dat',A0)


A0 = np.loadtxt('A0.dat')

















# plt.imshow(A0,cmap='YlGnBu',vmax=1,vmin=-1)
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.view_init(45,60)
ax.plot_surface(x, y, A0, rstride=1, cstride=1,cmap='rainbow',alpha=0.8)
plt.savefig('shock.png',dpi=600)
# plt.show()
exit()

	






