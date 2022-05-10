
nterms = int(input("Hvor mange tall vil du ha: "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Gi et positivt tall")
elif nterms == 1:
    print("Fibonacci tallrekken opp til", nterms, "tall:" )
    print(n1)
else:
    print("Fibonacci tallrekken opp til", nterms, "tall")
    while count <= nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1