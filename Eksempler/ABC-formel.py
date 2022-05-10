#abc formel matte
from pylab import *

a = float(input("Skriv inn A: "))
b = float(input("Skriv inn B: "))
c = float(input("Skriv inn C: "))

x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - sqrt(b**2-4*a*c))/(2*a)

i_rot=b**2-4*a*c

if i_rot < 0:
    print("Likningen har ikke løsninger ")
elif i_rot == 0:
    print("x = ", + x1)    
else:
    print ("Løsningen på denne ligningen er: ")
    print("x1 = ", x1, ", x2 = ", x2)
    
