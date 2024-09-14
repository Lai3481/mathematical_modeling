import cvxpy as cp
from numpy import array
from numpy import round

# min z= sum(i=1,4)sum(j=1,5)cij* xij
# s.t. {sum(i=1,4)xij =1 , j=1,2,..5 ,
#       sum(j=1,5)xij <=2, i=1,2,3,4 ,
#       xij = 1 or 0 , i=1,2,3,4 , j=1,2,..5}

# data
c=array([[15,13.8,12.5,11,14.3],
         [14.5,14,13.2,10.5,15],
         [13.8,13,12.8,11.3,14.6],
         [14.7,13.6,13,11.6,14]])

x=cp.Variable((4,5),integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
cons=[0<=x,x<=1,cp.sum(x,axis=0)==1,cp.sum(x,axis=1)<=2]

prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print('最优解为 \n',round(x.value,4))
print('最优值为 ',round(prob.value,4))