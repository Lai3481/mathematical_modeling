import numpy as np
import cvxpy as cp
import pylab as plt

# 题：有一定资金可用于投资，投资不同资产有相应风险，也有相应收益，
#     考虑投资越分散，总风险越小。购买资产要付交易费，
#     购买<定值时，按定值计算，假定银行利率5%，无风险无交易费。
# 问：如何风险尽可能小，收益尽可能大

# 符号：
# Si = 资产 ， i=0,1,2,...,n , S0 = 银行,
# xi = 投资量 ， i=0,1,2,...,n , x0 = 银行存款,
# ri = 平均收益，i=0,1,2,...,n ,
# qi = 风险损失，i=0,1,2,...,n , q0 = 0,
# pi = 交易费，  i=0,1,2,...,n , p0 = 0,
# ui = 投资阈值，i=0,1,2,...,n 

# 假设：
# 投资金额相当大 ==> 无上限
# 投资越分散，总风险越小 ==> 总风险可用所投最大qi
# 资产相互独立
# xi 可为任意值
# ri,qi,pi,ui 不变
# 不考虑其他费用，如印花税

# 建模：
# #总平均收益 = sum(0,n)rixi
# #交易费fi(xi) = {
# #0，xi=0,
# #piui, 0<xi<ui,
# #pixi, xi>=ui
# #}
# #总交易费 = sum(0,n)fi(xi)
# #投资所得（净收益）= sum(0,n)(rixi-fi(xi)) ==> sum(0,n)(ri-pi)xi
# #总体风险 = max(0,n)qixi
# #总资金 = sum(0,n)(1+pi)xi

# 最终模型：
# obj = min(max(0,n)qixi-sum(0,n)(ri-pi)xi),
# s.t.{
# sum(0,n)(1+pi)xi = M , M=总资金
# xi>=0, i=0,1,2,...,n }

# 具体求解：(线性化)
# 设置w = 投资偏好系数(0<=w<=1)
# obj ==> minw max(0,n)qixi-(1-w)sum(0,n)(ri-pi)xi)
# max(0,n)qixi转化为xn+1
#######模型结果#######
# obj =  minw xn+1-(1-w)sum(0,n)(ri-pi)xi)
# s.t. {
# qixi<=xn+1, i=0,1,2,...,n ,
# sum(0,n)(1+pi)xi = 10000, 
# xi>=0, i=0,1,2,...,n }

plt.rc('font',size=15)
plt.rc('font',family='SimHei')
# data
x=cp.Variable(6,pos=True)
r=np.array([0.05,0.28,0.21,0.23,0.25])
p=np.array([0,0.01,0.02,0.045,0.065])
q=np.array([0,0.025,0.015,0.055,0.026])

def LP(w):
    V=[] #risk
    Q=[] #gain
    X=[] #solution
    # sum(0,n)(1+pi)xi = 10000, qixi<=xn+1
    con=[(1+p)@x[:-1]==10000,cp.multiply(q[1:],x[1:5])<=x[5]]

    for i in range(len(w)):
        # obj =  minw xn+1-(1-w)sum(0,n)(ri-pi)xi)
        obj=cp.Minimize(w[i]*x[5]-(1-w[i])*(r-p)@x[:-1])
        prob=cp.Problem(obj,con)
        prob.solve(solver='GLPK_MI')

        xx=x.value  #get solution
        V.append(max(q*xx[:-1]))
        Q.append((r-p)@xx[:-1])
        X.append(xx)
    
    print('w = ',w)
    print('V = ',np.round(V,2))
    print('Q = ',np.round(Q,2))

    plt.figure();plt.plot(V,Q,'*-');plt.grid('on')
    plt.xlabel('风险/元');plt.ylabel('收益/元')
    return X

w1 = np.arange(0,1.1,0.1)
LP(w1);print('-----------------')

w2 = np.array([0.766,0.767,0.810,0.811,0.824,0.825,0.962,0.963,1.0])
X=LP(w2)
print('推荐方案 = ',X[-4]) #拐点/最佳投资方案
plt.show()
