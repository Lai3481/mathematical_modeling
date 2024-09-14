import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

# data
x0=np.arange(1,6)
y0=np.arange(1,4)
z0=np.array([[82,81,80,82,84],[79,63,61,65,81],[84,84,82,85,86]])

f=interp2d(x0,y0,z0)

# 插值点
xn=np.linspace(1,5,21)
yn=np.linspace(1,3,11)
zn=f(xn,yn)

# 预测的数值
x=np.array([1.5,1.5,2.5,2.5])
y=np.array([1.5,3.5,1.5,4.5])
z=np.zeros(4) #4个空位

for i in range(4):
    z[i]=f(x[i],y[i])

print(f'4个点的温度预测值为{z}')

# draw
X0,Y0=np.meshgrid(x0,y0)
Xn,Yn=np.meshgrid(xn,yn)
# 原图
ax1=plt.subplot(121,projection='3d')
ax1.plot_surface(X0,Y0,z0,cmap='viridis')
# 插值
ax2=plt.subplot(122,projection='3d')
ax2.plot_surface(Xn,Yn,zn,cmap='winter')
plt.show()