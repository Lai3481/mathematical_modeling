# runge kutta
# 种群竞争
# dx1/dt=r1x1(1-x1/N1-s1x2/N2),dx2/dt=r2x2(1-x2/N2-s2x1/N1)

from scipy.integrate import odeint
import pylab as plt
import numpy as np

# data
r1=2.5;r2=1.8;N1=1.6;N2=1;s1=0.25;s2=4

dx=lambda x,t:[r1*x[0]*(1-x[0]/N1-s1*x[1]/N2),
               r2*x[1]*(1-x[1]/N2-s2*x[0]/N1)]

t=np.linspace(0,8,50)
x=odeint(dx,[0.1,0.1],t)

plt.rc('font',size=16)
plt.plot(t,x[:,0],'-o',label='$x_1(t)$')
plt.plot(t,x[:,1],'-^',label='$x_2(t)$')
plt.xlabel('$t$');plt.legend()
plt.show()