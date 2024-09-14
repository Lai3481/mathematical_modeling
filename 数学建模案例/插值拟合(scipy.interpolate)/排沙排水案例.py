# 案例详解
# #通过实验记录黄河排水量及泥沙量数据，经过插值与拟合等方法
# 总结出每个时间点的排沙量及总排沙量
# 找出排水量与排沙量的关系

import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# 导入数据
# m**3/s
water = [1800,1900,2100,2200,2300,2400,2500,2600,2650,2700,2720,2650,2600,2500,2300,2200,2000,1850,1820,1800,1750,1500,1000,900] 
# kg/m**3
sand = [32,60,75,85,90,98,100,102,108,112,115,116,118,120,118,105,80,60,50,30,26,20,8,5] 

# 时间换算
i = np.arange(1,25)
t = (12*i-4)*3600 #以秒为单位

# 求排沙量
y = []
for i in range(0,24):
    y.append(water[i]*sand[i])
    print(f'时间：{t[i]}秒\n排沙量：{y[i]}kg\n')

# 插值
f = interp1d(t,y,'cubic') #三次样条
t1 = t[0];t2 = t[-1] #开始与结束时间

tt = np.linspace(t1,t2,10000) #插值节点

# 计算总排沙量 = 求插值函数的积分
TS = np.trapz(f(tt),tt)
print (f'总排沙量：{TS}kg')

# 使用拟合模型探讨排水量与排沙量的关系
nh1 = [];rmse1=np.zeros(2)
nh2 = [];rmse2=np.zeros(2)

for i in range(1,3):
    nh1=np.polyfit(water[:11],y[:11],i) #多项式拟合
    print(f'第一阶段{i}次多项式系数：{nh1}')
    yh1 = np.polyval(nh1,y[:11])    #求拟合的预测值
    cha1 = sum((y[:11]-yh1)**2)     #误差平方和
    rmse1[i-1]=np.sqrt(cha1/(10-i)) #平均差
print(f'剩余标准差分别为：{rmse1}')
print(f'\n第一阶段排沙量与排水量的预测模型为：sand = {nh1[0]}water**2 + {nh1[1]}water + {nh1[2]}\n')

for i in range(1,3):
    nh2=np.polyfit(water[11:],y[11:],i) #多项式拟合
    print(f'第一阶段{i}次多项式系数：{nh2}')
    yh2 = np.polyval(nh2,y[11:])    #求拟合的预测值
    cha2 = sum((y[11:]-yh2)**2)     #误差平方和
    rmse2[i-1]=np.sqrt(cha2/(10-i)) #平均差
print(f'剩余标准差分别为：{rmse2}')
print(f'\n第二阶段排沙量与排水量的预测模型为：sand = {nh2[0]}water**2 + {nh2[1]}water + {nh2[2]}\n')

# 作图
plt.rc('font',family='SimHei')
plt.rc('font',size=16)

# 排沙量对于时间
plt.subplot(131);plt.plot(t,y,'*')
plt.xlabel('时间与排沙量')
# 排沙量对于排水量
plt.subplot(132);plt.plot(water[:11],y[:11],'*')
plt.xlabel('排水量与排沙量第一阶段')
plt.subplot(133);plt.plot(water[11:],y[11:],'*')
plt.xlabel('排水量与排沙量第二阶段')
plt.show()