#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''
import numpy as np
import matplotlib.pyplot as plt
import easyraid.easyraid as erd


l = 200
P_tt = 20
pixels = 1024
Q = 1


l1 = 20
omega_1 = 3
plots_1 = 1000
l2 = 20
N = np.array([1,3,7])
E = erd.E2E(l,P_tt,pixels)

theta0,r0 = erd.E4H(Q,l1,omega_1,plots_1)

theta1,r1 = erd.Atenna(N=N[0],wavelength=l2,l=l1,plots=plots_1)
theta2,r2 = erd.Atenna(N=N[1],wavelength=l2,l=l1,plots=plots_1)
theta3,r3 = erd.Atenna(N=N[2],wavelength=l2,l=l1,plots=plots_1)


fig = plt.figure()

ax1 = plt.subplot(221,projection='polar')
ax1.plot(theta0,r0)
lines,labels = plt.thetagrids(range(0,360,90),())
ax1.set_title('quadrupole Electric raidiation')

ax2 = plt.subplot(222,projection='polar')
ax2.plot(theta1,r1)
lines,labels = plt.thetagrids(range(0,360,90),())
ax2.set_title('Atenna raidiation')

ax3 = plt.subplot(223,projection='polar')
ax3.plot(theta2,r2)
lines,labels = plt.thetagrids(range(0,360,90),())
ax3.set_title("{0} {1}".format('Atenna array,N=',N[1]))

ax4 = plt.subplot(224,projection='polar')
ax4.plot(theta3,r3)
lines,labels = plt.thetagrids(range(0,360,90),())
ax4.set_title('{} {}'.format('Atenna array,N=',N[2]))


fig.tight_layout()

plt.savefig('e4_raid&_Atennas_array.png',dpi=600)

plt.show()
exit()
