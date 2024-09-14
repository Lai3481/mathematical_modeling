import numpy as np

# 线性/一次插值
# 已知sqrt(100)=10,sqrt(121)=11，求sqrt(115)

x0=np.array([100,121])
y0=np.array([10,11])
q0=lambda x:x-x0[1]
q1=lambda x:x-x0[0]

y=q0(115)/q0(x0[0])*y0[0]+q1(115)/q1(x0[1])*y0[1]
print(np.round(y,4))

# 二次插值
# 已知sqrt(100)=10,sqrt(121)=11，sqrt(144)=12,求sqrt(115)
x1=np.array([100,121,144])
y1=np.array([10,11,12])
eq0=lambda x:(x-x1[1])*(x-x1[2])
eq1=lambda x:(x-x1[0])*(x-x1[2])
eq2=lambda x:(x-x1[0])*(x-x1[1])

y2=eq0(115)/eq0(x1[0])*y1[0]+eq1(115)/eq1(x1[1])*y1[1]+eq2(115)/eq2(x1[2])*y1[2]
print(np.round(y,4))
print(np.sqrt(115))
