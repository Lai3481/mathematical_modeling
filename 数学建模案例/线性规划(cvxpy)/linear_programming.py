# max z =70x1+50x2+60x3
# s.t. {2x1+4x2+3x3<=150 ,
#       3x1+x2+5x3<=160 ,
#       7x1+3x2+5x3<=200 , 
#       xi>=0, i=1,2,3}

import cvxpy as cp
from numpy import array
from numpy import round

c=array([70,50,60])

# s.t.
a=array([[2,4,3],[3,1,5],[7,3,5]]) #left
b=array([150,160,200]) #right

x=cp.Variable(3,pos=True) #3 instant variables
obj=cp.Maximize(c@x)    #target
cons=[a@x<=b]   

prob=cp.Problem(obj,cons)   
prob.solve(solver='GLPK_MI')

print('最优解为 ',round(x.value,4))
print('最优值为 ',round(prob.value,4))
