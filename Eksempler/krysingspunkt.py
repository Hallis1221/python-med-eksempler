from pylab import *

def differanse(x):
    return 0.32*x**2+6.18*x+1030-(20*sin(0.5*x)+9*x+1030)

startx = 0
sluttx = 10
dx = 1

while startx < sluttx:
    if differanse(startx)*differanse(startx+dx)<=0:
        print('Nullpunkt: ', startx)
    startx = startx + dx