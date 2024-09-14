import numpy as np
from scipy.optimize import minimize
from 料场供应 import df
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Microsoft Yahei', 'SimHei', 'sans-serif']

df2=pd.read_excel('非线性规划(scipy.optimize_minimize)\工地位置&水泥用量.xlsx')

a=df2.iloc[0,1:]
b=df2.iloc[1,1:]
c=df2.iloc[2,1:]
a=a.to_numpy()    #工地x坐标
b=b.to_numpy()    #工地y坐标
c=c.to_numpy()    #日用量

e=np.array([20,20]) #日储量

#xyz由np.random.randn(16)给随机数组
#x,y = 2*2  2个料场
#z=6*2 = 12
#xyz = 12+4=16
def obj(xyz): #离所有工地距离最近
    x=xyz[:2];y=xyz[2:4]
    z=xyz[4:].reshape(6,2) #水泥运输量
    obj=0
    for i in range(6):
        for j in range(2):
            obj+=z[i,j]*np.sqrt((x[j]-a[i])**2+(y[j]-b[i])**2)
    # obj: min z = sum(i=1,6)sum(j=1,2)cij*((ai-xj)**2+(bi-yj)**2)**0.5  

    return obj

con=[{'type':'eq','fun':lambda z:z[4:].reshape(6,2).sum(axis=1)-c},
    # sum(j=1,2)cij=di , i=1,2,...,6,   #运输量=日用量
     {'type':'ineq','fun':lambda z:e-z[4:].reshape(6,2).sum(axis=0)}]
    # sum(i=1,6)cij<=ej , j=1,2,        #运输量<=日储量

bd=[(0,11) for _ in range(16)] #对应xyz数量限制界限

res = minimize(obj,np.random.randn(16),constraints=con,bounds=bd)
print(res)

s=np.round(res.x,4)
print('目标函数的最优值：',round(res.fun,4))
print('料场A坐标：',[s[0],s[2]])
print('料场B坐标：',[s[1],s[3]])
print('料场到工地的运输量：\n',s[4:].reshape(6,2).T)

writer = pd.ExcelWriter('非线性规划(scipy.optimize_minimize)/料场数据.xlsx')

df2={
    '料场A':s[4:].reshape(6,2).T[0],
    '料场B':s[4:].reshape(6,2).T[1]
}

df2=pd.DataFrame(df2)

df2['料场A'].plot.bar(color='skyblue')
df2['料场B'].plot.bar(color='red')
plt.legend()
plt.xlabel('新建料场数据')
plt.ylabel('第 i 个工地')
plt.xticks(rotation=0)
plt.show()

# df.T.to_excel(writer,index=True,sheet_name='临时料场')
# df2.T.to_excel(writer,index=True,sheet_name='新建料场')
# writer._save()