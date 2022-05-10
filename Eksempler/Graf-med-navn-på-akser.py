from pylab import *

##def f(x) : #Definerer funksjoner
#    return 2*x**2+5*x

#x_val=linspace(-5,5,11)
#print(x_val)

#f_val=f(x_val)
#print(f_val)

#plot(x_val,f_val)

def f(x):
    return 0.5*x**3-3*x**2+5*x+100
def g(x):
    return 3*x**2+5*x+100

x_verdier=linspace(-2,8,101)

f_verdier = f(x_verdier)
g_verdier = g(x_verdier)

fig = plt.figure(figsize=(15,10))   #Størrelse graf
plot(x_verdier, f_verdier, color = "navy", label = "f(x)")
plot(x_verdier, g_verdier, color = "red", label = "g(x)")
legend()
xlabel("x")
ylabel("f(x) og g(x)")
title("Graf for f(x) = 0,5x^3-3x^2+5x-1")
grid(color = "yellow")
ylim(-5,210)
axhline(y=0,color="black")
axvline(x=0,color="black")