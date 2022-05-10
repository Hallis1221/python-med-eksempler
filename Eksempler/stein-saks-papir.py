
#tallet 1 skal bety saks.
#tallet 2 skal bety papir
#tallet 3 skal bety stein

saks = 1
papir = 2
stein = 3

datamaskinens_valg = 1

spillerens_valg = int(input("Skriv 1 for saks, 2 for papir, 3 for stein: "))

if spillerens_valg == 1:
    print("Datamaskinen valgte", datamaskinens_valg, "altså saks. Du valgte", saks, "altså saks. Det er likt!")
elif spillerens_valg == 2:
    print("Datamaskinen valgte", datamaskinens_valg, "altså saks. Du valgte", 2, "altså papir. Du tapte!")
elif spillerens_valg == 3:
    print("Datamaskinen valgte", datamaskinens_valg, "altså saks. Du valgte", stein, "altså stein. Du vant!")
else:
    print("Det var ikke en valgmulighet, velg enten 1, 2 eller 3!")