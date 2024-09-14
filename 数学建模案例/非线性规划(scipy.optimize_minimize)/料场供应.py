import numpy as np
import pandas as pd
import cvxpy as cp
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Microsoft Yahei', 'SimHei', 'sans-serif']

data=pd.read_excel('非线性规划(scipy.optimize_minimize)\工地位置&水泥用量.xlsx')

# 题：
# 6个工地，位置：(ai,bi)，临时料场A(5,1),B(2,7)，日储量20吨
# 问：
# 1. 每日供应计划，吨/km 最小
# 2. 新建2个料场取代A,B，求位置

# 假设：各料场到各工地直线连接

# 符号：
# (ai,bi) = 工地位置，i=1,2,...,6,
# di = 水泥日用量，i=1,2,...,6,
# (xj,yj) = 料场位置，j=1,2,
# ej = 料场日储量，j=1,2,
# cij = 水泥运输量，i=1,2,...,6,j=1,2

# 模型：
# obj: min z = sum(i=1,6)sum(j=1,2)cij*((ai-xj)**2+(bi-yj)**2)**0.5 ,
# s.t.{
# sum(i=1,6)cij<=ej , j=1,2,        #运输量<=日储量
# sum(j=1,2)cij=di , i=1,2,...,6,   #运输量=日用量
# cij>=0 ,i=1,2,...,6,j=1,2         
# }

a=data.iloc[:,1:]
ab=a.iloc[:2,:].T
d=a.iloc[2,:]

ab=ab.to_numpy()
d=d.to_numpy()
g=[[5,1],[2,7]] #料场坐标

r=[[np.linalg.norm(ab[i]-g[j]) for i in range(6)] for j in range(2)] #距离
r=np.array(r)

c=cp.Variable((2,6),pos=True)
obj=cp.Minimize(cp.sum(cp.multiply(r,c)))
con=[cp.sum(c,axis=1)<=20,cp.sum(c,axis=0)==d]

prob=cp.Problem(obj,con)
prob.solve(solver="GLPK_MI")
print('最优值：',prob.value)
print('最优解：\n',c.value)

df={
    '料场A':c.value[0],
    '料场B':c.value[1]
}

df=pd.DataFrame(df)
df['料场B'].plot.bar(color='red')
df['料场A'].plot.bar(color='skyblue')

plt.legend()
plt.xlabel('临时料场数据')
plt.ylabel('第 i 个工地')
plt.xticks(rotation=0)
plt.show()

# writer._save()