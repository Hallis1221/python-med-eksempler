from pylab import *

def f(x):
    return (3*x-6)/(6*x+4)
x_verdier = linspace(-10, -2/3, 2000)
x2=linspace(-2/3,10,1000)
f_verdier = f(x_verdier)
f2_verdier = f(x2)

fig = plt.figure(figsize=(15,10))  
plot(x_verdier, f_verdier, color = "navy")
plot(x2, f2_verdier, color = "navy")
ylim(-10,10)

axhline(y=0,color="black")
axvline(x=0,color="black")

axhline(y=1/2, color = "green", linestyle = "dashed")
axvline(x=-2/3, color = "green", linestyle = "dashed")