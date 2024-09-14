import numpy as np
import pylab as plt
from scipy.interpolate import lagrange

y=lambda x:1/(1+x**2)
x0=np.linspace(-5,5,100)  
x1=np.linspace(-5,5,3)  #3个节点
x2=np.linspace(-5,5,5)  #5个节点
x3=np.linspace(-5,5,7)  #7个节点

y1=lagrange(x1,y(x1))   #插值2次多项
y2=lagrange(x2,y(x2))   #插值4次多项
y3=lagrange(x3,y(x3))   #插值6次多项

plt.plot(x0,y(x0))  #正确图形
plt.plot(x0,np.polyval(y1,x0),'--*b')
plt.plot(x0,np.polyval(y2,x0),'-.')
plt.plot(x0,np.polyval(y3,x0),'-p')
plt.legend(['$1/(1+x^2)$','$n=2$','$n=4$','$n=6$'])
plt.show()