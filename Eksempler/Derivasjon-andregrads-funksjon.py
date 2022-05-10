from pylab import *

a = float(input("A leddet i 2. gradsfunksjonen: "))
b = float(input("B leddet i 2. gradsfunksjonen: "))

a2 = str(a*2)

if b >= 0:
    b = str(b)  

    print(a2 + "x " + "+ " + b)
else:
    b = str(b)  
    print("Funksjonen for derivasjonslinjen er: " + a2 + "x " + b.replace("-", "- ")) 
    

a = float(a)
derivverdix = float(input("For hvilken x verdi, ønsker du å vite stigningstall?: "))
c = str(a*derivverdix)
derivverdix = str(derivverdix)
print("Stigningstallet i grafen når x = " + derivverdix + " er " + c)  
               
    
     
 