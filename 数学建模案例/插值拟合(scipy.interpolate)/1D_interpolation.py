import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 凌晨1点到中午12点测量温度，估计每0.1小时的温差并作出温度变化图

x0=np.arange(1,13) 
y0=np.array([5,8,9,15,25,29,31,30,22,25,27,24]) #数据

x1=np.linspace(1,12,101)    #插值点
f1=interp1d(x0,y0);y1=f1(x1)            #分段插值
f2=interp1d(x0,y0,'cubic');y2=f2(x1)    #三次插值

x2=np.array([3.2,5.6,7.8,11.5]) #问
yh1=f1(x2)  #分段预测值
yh2=f2(x2)  #三次预测值
print('分段插值预测值：',yh1)
print('三次插值预测值：',np.round(yh2,4))

plt.rc('font',size=16);plt.rc('font',family='SimHei')
plt.subplot(121);plt.plot(x1,y1);plt.xlabel('(A)分段线性插值')
plt.subplot(122);plt.plot(x1,y2);plt.xlabel('(B)三次样条插值')
plt.show()