import cvxpy as cp
import numpy as np

# xi = {1, company choosed, 0 ,else}, i=1,2,3 = a,b,c
# yi = duration phone call
# obj = min 16x1 + 25x2 + 18x3 + 0.25y1 + 0.21y2 + 0.22y3
# s.t. {sum(yi)=200,
#       yi=0,xi=0}

x=cp.Variable((2,3),integer=True)

a=np.array([[16,0.25],[25,0.21],[18,0.22]])

obj=cp.Minimize(cp.sum(a@x))

# cons=[x>=0,cp.sum(x,axis=0)<=200,x[1][0]+x[1][1]+x[1][2]==200]

# prob=cp.Problem(obj,cons)
# prob.solve(solver='GLPK_MI')

# print(x.value,prob.value)