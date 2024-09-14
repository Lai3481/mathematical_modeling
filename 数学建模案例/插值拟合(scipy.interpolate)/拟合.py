import numpy as np
from scipy.optimize import curve_fit
import pylab as plt

# linear
x0=np.array([1,3,4,5,6,7,8,9,10])
y0=np.array([10,5,4,2,1,1,2,3,4])
p=np.polyfit(x0,y0,2)   #2次多项式拟合

print('从高幂到低幂系数为',np.round(p,4))

# curve
t0=np.arange(0,2.1,0.1)
y0=np.array([5.8955,3.5639,2.5173,1.979,1.899,1.3938,1.1359,1.0096,
             1.0343,0.8435,0.6856,0.61,0.5392,0.3946,0.3903,0.5474,
             0.3459,0.173,0.2211,0.1704,0.2636])

def get_polyfit_equation(t,b1,b2,L1,L2):
    return b1*np.exp(-L1*t)+b2*np.exp(-L2*t) #返回拟合多项式

popt,pcov=curve_fit(get_polyfit_equation,t0,y0)
print('b1,b2,L1,L2 的拟合值为 ',np.round(popt,4))

yh=get_polyfit_equation(t0,*popt) #计算已知数据预测值以构建图形
plt.rc('font',size=16);plt.rc('font',family='SimHei')
plt.plot(t0,y0,'o')
plt.plot(t0,yh)
plt.legend(['已知','拟合'])
plt.show()
