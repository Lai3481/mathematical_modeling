import sympy as sp

# y.diff(x,3)-y.diff(x,2)=x

x=sp.var('x') #变量
y=sp.Function('y') #求解的

eq=y(x).diff(x,3)-y(x).diff(x,2)-x
# initial values
con={y(1):8,
     y(x).diff(x).subs(x,1):7,
     y(x).diff(x,2).subs(x,2):4}

s=sp.dsolve(eq,ics=con)
print(s)

# 方程组
# dx/dt = 2x-3y+3z
# dy/dt = 4x-5y+3z
# dz/dt = 4x-4y+2z

t=sp.var('t');x,y,z=sp.var('x,y,z',cls=sp.Function)
eqs=[x(t).diff(t)-2*x(t)+3*y(t)-3*z(t),
     y(t).diff(t)-4*x(t)+5*y(t)-3*z(t),
     z(t).diff(t)-4*x(t)+4*y(t)-2*z(t)]

s1=sp.dsolve(eqs)
print(s1)
