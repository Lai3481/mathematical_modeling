# let xi = {1, station in town , 0 , station not in town}, i =1,2,...,6
# obj = min sum(xi)
# yij = {1, driving time from i to j<= 18 , 0, else}
# s.t.  xi,xj >= 1 when yij =1

import cvxpy as cp
import numpy as np

# var
x=cp.Variable(6,integer=True)
y=[[0,19,23,18,20,25],
   [19,0,22,13,22,11],
   [23,22,0,60,17,20],
   [18,13,60,0,55,17],
   [20,22,17,55,0,12],
   [25,11,20,17,12,0]]

obj=cp.Minimize(cp.sum(x))

for i,b in enumerate(y):
    for j,a in enumerate(b):
        if a<=18:
            y[i][j]=1
        else:
            y[i][j]=0

cons=[np.array(y)@x>=1,x>=0]

prob=cp.Problem(obj,cons)
prob.solve(solver="GLPK_MI")

print(x.value,prob.value)