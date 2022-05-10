from pylab import * 

a=1
b=1
c=2
d=3
e=3
f=6

if (-d*b+e*a) == 0:
    print("Det er ikke nok gyldig info til å løse videre")
else:
    y = (a*f - d*c)/(-d*b+e*a)
    x = c/a - b/a*y
    print("Y = ", y, "X = ", x)

