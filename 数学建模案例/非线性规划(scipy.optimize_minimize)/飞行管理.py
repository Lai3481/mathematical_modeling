import numpy as np
from scipy.optimize import minimize

# 题：
# 万米高空，边长160公里的正方形区域，判断飞机之间碰撞可能，如有则应调整方向
# 问：
# 最优调整方案

# 假设：
# 飞行高度 = 10000米，飞行速度 = 800千米/小时
# 忽略转弯半径影响，飞行方向瞬时调整
# 每架飞机最多调整一次方向，幅度<=pi/6
# 安全距离>8000米
# 每架飞机近似质点
# 不考虑飞机离开正方形区域后的飞行状况

# 符号：
# L = 管理区域边长 = 160千米
# D = 管理区域 = [0,L]*[0,L]
# v = 飞行速度 = 800千米/小时
# N = 飞机数， N为即将进入区域的飞机
# (xi0,yi0) = 飞机起始位置      i=1,2,...,N,
# (xit,yit) = 飞机t时刻位置     i=1,2,...,N,
# Ti = 飞行时长
# ai = 原飞行角度               0<=ai0<2pi
# bi = 调整幅度                 i=1,2,...,N,
# ci = ai + bi = 调整后角度     i=1,2,...,N,     
  
# 建模：
# rij = 飞机之间距离
# (xit,yit) = (xi0+vt cos ai , yi0+vt sin ai)
# 距离公式：
# rijt**2 = (xit-xjt)**2+(yit-yjt)**2   
######################
# 得出
# 确保安全距离：rijt**2 = dij*t**2+eijt+rij0**2
######################
# dij = v**2[(cos ai -cos aj)**2+(sin ai - sin aj)**2]
# eij = 2v[(xi0-xj0)(cos ai-cos aj)+(yi0-yj0)(sin ai - sin aj)]
# rij0**2 = (xi0-xj0)**2+(yi0-yj0)**2
######################
# 关于安全距离限制：rijt**2 = dijt**2+eijt**2+rij0**2 > 64
######################
# 考虑飞行时间：
# Ti = min{t>0: xi0+vt cos ai = 0/160 || yi0+vt sin ai = 0/160} #飞出任意条边
# 记 Tij = min[Ti,Tj] 保证飞机之间不碰撞
# t <= Tij

# 模型：
# obj: min f = sum(1,N)(bi)**2  #总调整应取|bi|,为方便计算取bi**2
# s.t.{
# rijt**2> 64  i=1,2,...,N, j=1,2,...,N, i!=j,
# t <= Tij     i=1,2,...,N, j=1,2,...,N, i!=j,
# |bi|<= pi/6  i=1,2,...,N  }

# data
t0 = np.array([243,236,220.5,159,230,52])/180*np.pi
x0 = np.array([150,85,150,145,130,0])
y0 = np.array([140,85,155,50,150,0])

obj = lambda t:sum(t**2)
con=[]

######################
# dij = v**2[(cos ai -cos aj)**2+(sin ai - sin aj)**2]
# eij = 2v[(xi0-xj0)(cos ai-cos aj)+(yi0-yj0)(sin ai - sin aj)]
# rij0**2 = (xi0-xj0)**2+(yi0-yj0)**2
######################
for i in range(5):
    for j in range(i+1,6):
        con.append({'type':'ineq','fun':lambda t:
                    (4*(np.sin(t0[i]+t[i]-t0[j]-t[j])/2)**2*
                    ((x0[i]-x0[j])**2+(y0[i]-y0[j])**2-64)-
                    # 由来：
                    # rijt**2 = (xit-xjt)**2+(yit-yjt)**2  > 64 
                    #         = dij*t**2+eijt+rij0**2 - 64
                    ((x0[i]-x0[j])*(np.cos(t0[i]+t[i])-
                    np.cos(t0[j]+t[j]))-((y0[i]-y0[j])*
                    np.sin(t0[i]+t[i])-np.sin(t0[j]+t[j]))))**2})
                    # [(xi0-xj0)(cos ai-cos aj)+(yi0-yj0)(sin ai - sin aj)]


#|bi|<= pi/6 <==> -np.pi/6<=bi<=np.pi/6
bd = [(-np.pi/6,np.pi/6) for i in range(6)]
res = minimize(obj,np.random.rand(6),constraints=con,bounds=bd)

print(res)
print('最优值：',round(res.fun,10))
print('最优解：\n',res.x/np.pi*180)
