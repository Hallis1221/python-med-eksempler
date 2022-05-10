from pylab import*

PQ = 150
QR = 360
PR = 390

if PR**2 == QR**2 + PQ**2:
    print("Trekant PQR er rettvinklet ettersom pytagoras setning fungerer.")
    if PR == PQ*2:
        print("Trekant PQR er i tillegg til en rettvinklet trekant en 30, 60, 90 trekant ettersom hypotenusen er dobbelt så lang som korteste katet")
    else: print("Den er likevel ikke en 30, 60, 90 trekant, ettersom hypotenusen ikke er dobbelt så lang som korteste katet")
else:
    print("Trekant PQR er ikke rettvinklet ettersom pytagoras setning ikke fungerer")