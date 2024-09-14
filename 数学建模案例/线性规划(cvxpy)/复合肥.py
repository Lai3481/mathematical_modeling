import pandas as pd
import cvxpy as cp

data = pd.read_excel('线性规划(cvxpy)\复合肥数据.xlsx')

# 问：最低成本&复合肥各个元素用量

# 假设：
# 1 没有养分流失
# 2 含水量<=2%
# 3 3%<=含氯量<=15%
# 4 水分蒸发可控

# 符号：
# xi = 原料 ，i=1,2,3,..,8
# aij = 原料成分百分比 ， i=1,2,3,..,8, j=1,2,3,4,5
# pi = 市场价格 ， i=1,2,3,..,8
# m = 水分蒸发量

# 建模：
# obj : min z= sum(1,8)pixi
# constraint : {
# sum(i=1,8)aijxi=0.15 , j=1,2,3,
# ######水分######
# {0<=m<=1000y,
# m>=sum(1,8)ai4xi-0.02,
# m<=sum(1,8)ai4xi-0.02+1000(1-y),
# y=0/1},
###################
# sum(1,8)xi-m=1,
# 0.03<=sum(1,8)ai5xi<=0.15,
# xi>=0, i=1,2,3,..,8
# }

# loc data
a=data.iloc[1:,1:-1]
price=data.iloc[1:,-1]

list_a=a.to_numpy() 
list_p=price.to_numpy()

# print(type(price.items))
# build var
x=cp.Variable(8,pos=True)
m=cp.Variable(1,pos=True)
y=cp.Variable(1,integer=True)

# obj and cons
obj=cp.Minimize(list_p@x)
con=[y>=0,y<=1,m<=1000*y]

for j in range(3):
    con.append(list_a[:,j]@x*0.01==0.15)

con.append(m>=list_a[:,3]@x*0.01-0.02)
con.append(m<=list_a[:,3]@x*0.01-0.02+1000*(1-y))
con.append(cp.sum(x)-m==1)
con.append(0.03<=list_a[:,4]@x*0.01)
con.append(list_a[:,4]@x*0.01<=0.15)

# solve
prob1=cp.Problem(obj,con)
prob1.solve(solver='GLPK_MI')

print('最优值为：',prob1.value)
print('最优解为：单位(kg)\n',x.value*1000,'\n水分含量 = ',m.value)

if y.value == 0:
    print('\n是否需要烘干 = 否')
elif y.value == 1:
    print('\n是否需要烘干 = 是')

# change value of price
p2=list_p.copy()
p2[3]=618

obj2=cp.Minimize(p2@x)
prob2=cp.Problem(obj2,con)
prob2.solve(solver="GLPK_MI")
print('------------------------')
print('新最优值为：',prob2.value)
print('新最优解为：单位(kg)\n',x.value*1000,'\n水分含量 = ',m.value)

if y.value == 0:
    print('\n是否需要烘干 = 否')
elif y.value == 1:
    print('\n是否需要烘干 = 是')

