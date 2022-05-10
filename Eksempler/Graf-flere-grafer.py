from pylab import*

def f(x):
    return 3*x + 3
def g(x):
    return -2*x + 28
def h(x):
    return 8*x + 28
def i(x):
    return 4*x + 28
def j(x):
    return 14*x + 58

fig = plt.figure(figsize=(15,10))  

x_val = linspace(-5, 5, 100)
f_val = f(x_val)

x2_val = linspace(0, 5, 100)
g_val = g(x2_val)

x3_val = linspace(-5, 0, 100)
h_val = h(x3_val)

x4_val = linspace(-3, 0, 100)
i_val = i(x4_val)

x5_val = linspace(-5, -3, 100)
j_val = j(x5_val)

plot(x_val, f_val, label = "f(x)")
plot(x2_val, g_val, label = "g(x)")
plot(x3_val, h_val, label = "h(x)")
plot(x4_val, i_val, label = "i(x)")
plot(x5_val, j_val, label = "j(x)")

legend()
grid(color = "gray")
axhline(y=0, color = "Black")
axvline(x=0, color = "Black")