'''
甲舰于O点（0，0）发射导弹追踪乙舰 A（1，0）
乙舰向着 y = x-1 方向以速度v前进
导弹速度为5v
何处击中乙舰？
'''

# 建模
# (1-x)y''=1/5(1+y**2)**0.5

from scipy.integrate import odeint
import pylab as plt
import numpy as np

dy = lambda y,x:[y[1],np.sqrt(1+y[0]**2)/5/(1-x)]
x=np.arange(0,1,0.0001)

y=odeint(dy,[0,0],x)
plt.rc('font',size=16)
plt.plot(x,y[:,0])
plt.plot([1,1],[0,0.2],'--k')
plt.show()



