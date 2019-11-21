#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

pixels = 1024
halfp = int(pixels/2)
omega = 0.01
pi = np.pi
l = 300#wave length
k= 2*pi/l#wave number

E = np.zeros(shape=(pixels,pixels),dtype='complex')#complex electric field intensity
E_L = np.zeros(pixels,dtype='complex')

E_file = './E_map.dat'
E_0 = np.loadtxt(E_file,dtype='complex')

E_L[:] = E_0[0,:]


fig = plt.figure()
ell = np.arange(-1*halfp,halfp,1)

line, = plt.plot(ell, E_L[ell],'b-')
plt.ylim(ymin=-0.005,ymax=0.005)


def animate(i):
    line.set_ydata(np.cos(k*abs(ell) - omega*i)*ell/abs(ell)/(abs(ell)+1000))
    return line,

ani.FuncAnimation(fig, animate, np.arange(0,1000),interval=25, blit=True)

plt.show()