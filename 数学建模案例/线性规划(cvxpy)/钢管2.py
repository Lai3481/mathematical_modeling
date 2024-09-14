import numpy as np
import cvxpy as cp

# 题：钢管（未切割）= 19m，顾客要求50*4m,20*6m,15*8m + (10*5m), 切割模式<=3
# 问：如何切割余料最省

# 假设：
# 1 过程无损，无此品
# 2 余料不重复利用
# 3 4m,6m,8m可>需求
# 4 5m=10

# 符号:
# xi = 原料根数 , i=1,2,...,16
# ri = 余料长度 , i=1,2,...,16
# dj = 顾客需求 , j=1,2,3,4
# aij = i模式下j长度钢管数量 , i=1,2,...,16 , j=1,2,3,4
# yi = {1, 使用模式
#       0, 不使用 , i=1,2,...,16}

# 建模:
# obj: min z = sum(1,7)rixi (余料最少)
# constraints:{
# sum(1,16)aijxi>=dj, j=1,2,3,4,
# sum(1,16)ai4xi=10 ,
# sum(1,16)yi<=3,
# xi<=100yi, i=1,2,...,16, (表示一个充分大的数)(因为计算余料最少可能导致原料使用过度)
# xi>=0 , i=1,2,...,16,
# yi=1/0 , i=1,2,...,16}

mode=[];r=[]
# 从枚举法得知切割4种长度钢管有16种模式, 粗略计算各个长度出现次数(模式数)
# 通过循环,寻找符合标准的模式并计算余料
for i in range(5): #4m num
    for j in range(4): #6m num
        for k in range(3): #8m num
            for m in range(4): #5m num
                if 4*i+6*j+8*k+5*m>15 and 4*i+6*j+8*k+5*m<=19:
                    mode.append([i,j,k,m])
                    r.append(19-4*i-6*j-8*k-5*m)

a=np.array(mode).T;res=np.array(r)
d=[50,20,15]

x=cp.Variable(16,integer=True)
y=cp.Variable(16,integer=True)
obj=cp.Minimize(res@x)
con=[y>=0,y<=1,a[:3,:]@x>=d,a[-1,:]@x==10,sum(y)<=3,x>=0,x<=100*y]

prob=cp.Problem(obj,con)
prob.solve(solver='GLPK_MI')

print('最优值为：',prob.value)
print('最优解为：\n',x.value)
print('余料长度为：\n',res@x.value)
print('四种短钢管数量为：\n',a@x.value)