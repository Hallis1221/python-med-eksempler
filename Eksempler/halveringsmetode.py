from pylab import *

def f(t):
    return -10*t**2 + 20*t

nedregrense = 0.1
øvregrense = 10.1
nøyaktighet = 0.01
telling = 0

a = nedregrense
b = øvregrense
m = (a+b)/2

while telling <= 10:
 
    if f(a) * f(m) < 0:
        b = m
    else:
        a=m
    m = (a+b)/2   
    telling = telling + 1     


print (f'Løsningen til likniningen er x = {m: .1f}.!')
