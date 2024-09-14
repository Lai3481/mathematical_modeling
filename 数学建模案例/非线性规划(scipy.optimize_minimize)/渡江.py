import numpy as np
from scipy.optimize import minimize

# 题：
# 河道宽1160米，终点于河对岸平行方向1000米
# 问：
# 1 水流速1.89米/秒，挑战者成绩14分8秒，速度及方向？
# 2 水流速v(y) = {1.47m/s , 0<=y<=200,
#                2.11m/s , 200<y<960,
#                1.47m/s , 960<=y<=1160},
# 挑战者速度1.5米/秒，方向和路线？

# 符号：
# u = 游泳速度
# v = 水流速度
# H = 河宽
# L = 起点的正对岸到终点的水平距离
# T = 时间
# a = 方向夹角

# （1）
# T = H/(u cos a )= L/(v-u sin a)
# u = ((H/T)**2+(v-L/T)**2)**0.5 = 1.5416
# a = arctan((VT - L)/H) = 0.4792

# (2)
# T = sum(1,3)ti
# s.t.{
# (t1+t3)1.5cos a1 = 400 , 
# t2*1.5cos a2 = 760 ,
# (1.47-1.5sin a1)(t1+t3)+(2.11-1.5sin a2)t2 = 1000,
# t1=t3 , 
# ti>=0 , i=1,2,3,
# 0<=ai<=pi/2 , i=1,2}

obj = lambda x:2*x[0]+x[1]
con = [{'type':'eq','fun':lambda x :2*x[0]*1.5*np.cos(x[2])-400},
       {'type':'eq','fun':lambda x :x[1]*1.5*np.cos(x[3])-760},
       {'type':'eq','fun':lambda x :(1.47-1.5*np.sin(x[2]))*2*x[0]+(2.11-1.5*np.sin(x[3]))*x[1]-1000}]

LB = [0]*4 ; UB=[np.inf,np.inf,np.pi/2,np.pi/2] #4种类型数据上下限
bd=list(zip(LB,UB))

x=minimize(obj,np.random.rand(4),constraints=con,bounds=bd)
print(x);print('角度： ',x.x[2:]*180/np.pi)