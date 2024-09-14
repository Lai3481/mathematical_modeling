import pandas as pd
import cvxpy as cp

data=pd.read_excel('线性规划(cvxpy)\钢管切割数据.xlsx')

# 题：钢管（未切割）= 19m，顾客要求50*4m,20*6m,15*8m
# 问：如何切割原料最省

# 假设：
# 1 过程无损，无此品
# 2 余料不重复利用
# 3 4m,6m,8m可>需求

# 符号:
# xi = 原料根数 , i=1,2,...,7
# ri = 余料长度 , i=1,2,...,7
# dj = 顾客需求 , j=1,2,3
# aij = i模式下j长度钢管数量 , i=1,2,...,7 , j=1,2,3

# 建模:
# obj: min z = sum(1,7)rixi (余料最少)
# obj: min z = sum(1,7)xi (原料最少)
# constraints:{
# sum(1,7)aijxi>=dj, j=1,2,3,
# xi>=0 , i=1,2,...,7}

a=data.iloc[:,1:-1].T
r=data.iloc[:,-1]

list_a=a.to_numpy() 
list_r=r.to_numpy() 
d=[50,25,15]

x=cp.Variable(7,integer=True)
obj=cp.Minimize(list_r@x)

con=[x>=0,list_a@x>=d]
prob=cp.Problem(obj,con)
prob.solve(solver='GLPK_MI')

print('最优值为：',prob.value)
print('最优解为：\n',x.value)
print('三种短钢管数量为：\n',list_a@x.value)

obj2=cp.Minimize(sum(x))
prob2=cp.Problem(obj2,con)
prob2.solve(solver='GLPK_MI')
print('----------------------')
print('最优值为：',prob2.value)
print('最优解为：\n',x.value)
print('余料长度为：\n',list_r@x.value)
print('三种短钢管数量为：\n',list_a@x.value)
