# 案例解析
'''
HIV病毒感染免疫T细胞引发艾滋病感染
T细胞由骨髓造出，或通过自身繁衍
HIV病毒感染正常T细胞后，将潜伏在T细胞中一段时间，
之后可能转化成活性感染细胞
研究各个细胞的变化量，推导HIV病毒与T细胞浓度的关系模型
'''

# 建模
'''
记 s为新T细胞产生速率，r为T细胞的最大繁殖率，Tm为T细胞最大浓度，V为HIV病毒浓度，
m1为正常T细胞的死亡率，m2为活性感染细胞的死亡率，mv为HIV病毒的自然清除率，
k1为正常T细胞被感染的概率常数，k2为被潜伏T细胞的活性转化概率常数，
N为病毒复制数
'''

# 由此可得方程（对时间变化微分）：
'''
  dT1（正常T细胞）= s + rT1(1-(T1+T2+T3)/Tm) - m1T1 - k1T1V ,
  dT2（被潜伏T细胞）= k1T1V - m1T2 - k2T2 ,
  dT3（活性感染T细胞）= k2T2 - m2T3 ,
  dV（HIV病毒）= Nm2T3 - k1T1V - mvV
'''


# 程序
from scipy.integrate import odeint

import numpy as np
import matplotlib.pyplot as plt

# data
s=10;r=0.03;tm=1500;m1=0.02;m2=0.24
mv=2.4;k1=2.4e-5;k2=3e-3

# equation
dy=lambda x,t,n:[s+r*x[0]*(1-(x[0]+x[1]+x[2])/tm)-m1*x[0]-k1*x[0]*x[3],
                 k1*x[0]*x[3]-m1*x[1]-k2*x[1],k2*x[1]-m2*x[2],
                 n*m2*x[2]-k1*x[0]*x[3]-mv*x[3]]

# define time
t=np.arange(0,3000,100)

# define intial value
# x[0]=T1 , x[1]=T2 , x[2]=T3 , x[3]=V
x0=np.array([1000,0,0,1e-3])

# solve equation
# args = n
s1=odeint(dy,x0,t,args=(1400,))
s2=odeint(dy,x0,t,args=(1000,))
s3=odeint(dy,x0,t,args=(600,))

# plot graph
s=['o-','*-','s-']
plt.rc('font',family='SimHei')
plt.rc('font',size=16)

def plotfun(s1,s2,s3,i):
    plt.plot(t,s1[:,i-1],s[0],label='$N=1400$')
    plt.plot(t,s2[:,i-1],s[1],label='$N=1000$')
    plt.plot(t,s3[:,i-1],s[2],label='$N=600$')
    plt.legend()

# adjust linespacing
plt.subplots_adjust(hspace=0.3)

# final
plt.subplot(221);plotfun(s1,s2,s3,1)
plt.title('$T_1(t)$')
plt.subplot(222);plotfun(s1,s2,s3,2)
plt.title('$T_2(t)$')
plt.subplot(223);plotfun(s1,s2,s3,3)
plt.title('$T_3(t)$')
plt.subplot(224);plotfun(s1,s2,s3,4)
plt.title('$V(t)$')

plt.show()