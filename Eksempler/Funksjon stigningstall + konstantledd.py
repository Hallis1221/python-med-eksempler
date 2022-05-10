
x1 = float(input("Skriv inn x1: "))
y1 = float(input("Skriv inn y1: "))
x2 = float(input("Skriv inn x2: "))
y2 = float(input("Skriv inn y2: "))

stigningstall = ((y2-y1)/(x2-x1))
konstantledd = (y1-(stigningstall*x1))

stigningstall = str(stigningstall)
konstantledd = str(konstantledd)

print("Stigningstallet er: " + stigningstall)
print("Konstantleddet er: " + konstantledd)