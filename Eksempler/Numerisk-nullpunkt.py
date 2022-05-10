from pylab import *

def h(x):
    return 4*x

def f(x):
    return 2**x-12

def g(x):
    return f(x)-h(x)

xstart = 0
hopp = 0.0001

while f(xstart)*f(xstart + hopp)>0: #Endre til g hvis jeg skal kjøre krysingspunkt
    xstart = xstart + hopp


print(xstart)
print(g(xstart))