def summiereAlleZahlenInListe(liste):
    zwischensumme = 0
    for zahl in liste:
        zwischensumme += zahl
    return zwischensumme

def ermittleGroessteZahlInListe(liste):
    bisherGroessteZahl = liste[0]
    for zahl in liste:
        if zahl > bisherGroessteZahl:
            bisherGroessteZahl = zahl
    return bisherGroessteZahl

def multipliziereAlleZahlenInListe(liste):
    summe = 1
    for zahl in liste:
        summe *= zahl
    return summe
    #return math.prod(liste)

def ermittleKleinsteZahlInListe(liste):
    bisherKleinsteZahl = liste[0]
    for zahl in liste:
        if zahl < bisherKleinsteZahl:
            bisherKleinsteZahl = zahl
    return bisherKleinsteZahl
    #return min(liste)

def istListeLeer(liste):
    return len(liste) == 0

def ermittleIndexDerKleinstenZahl(liste):
    return liste.index(ermittleKleinsteZahlInListe(liste))

def gibVerdoppelteListeZurueck(liste):
    return [zahl*2 for zahl in liste]

def zaehleZweistelligeZahlen(liste):
    return len([zahl for zahl in liste if len(str(abs(zahl)))==2])

def entferneGeradeZahlen(liste):
    for zahl in liste:
        if zahl%2 == 0:
            liste.remove(zahl)
    # return [i for i in liste if i%2==0] # Falls die Originale Liste nicht verändert werden soll
    
def sindAlleZahlenPositiv(liste):
    isPositiv = True
    for zahl in liste:
        if abs(zahl) != zahl:
            isPositiv = False
    return isPositiv

def mehrPositiveOderNegativeZahlen(liste):
    pos = [zahl for zahl in liste if abs(zahl) == zahl]
    neg = [zahl for zahl in liste if abs(zahl) != zahl]
    if len(pos) > len(neg): return "Die Liste hat mehr positive als negative Zahlen"
    elif len(pos) < len(neg): return "Die Liste hat mehr negative als positive Zahlen"
    else: return "Die Liste hat gleich viele positive und negative Zahlen"
    
def enthaeltDuplikate(liste):
    doubles = False
    for zahl in liste:
        if liste.count(zahl) > 1: doubles = True
    return doubles
    # return len([zahl for zahl in liste if liste.count(zahl) > 1]) > 0
    

zahlenliste = [5, 2, 9, 13, 16, 27, 1, 67, 12, 56]

summeDerZahlenliste = summiereAlleZahlenInListe(zahlenliste)
print(f"Die Summe aller Zahlen in der Zahlenliste ist {summeDerZahlenliste}")

groessteZahlInZahlenliste = ermittleGroessteZahlInListe(zahlenliste)
print(f"Die größte Zahl in der Zahlenliste ist {groessteZahlInZahlenliste}")

produktDerZahlenliste = multipliziereAlleZahlenInListe(zahlenliste)
print(f"Das Produkt aller Zahlen in der Zahlenliste ist {produktDerZahlenliste}")

kleinsteZahlInZahlenliste = ermittleKleinsteZahlInListe(zahlenliste)
print(f"Die kleinste Zahl in der Zahlenliste ist {kleinsteZahlInZahlenliste}")

isEmpty = istListeLeer(zahlenliste)
print("Die Liste ist Leer." if isEmpty else "Die Liste ist nicht Leer.")

print(f"Der Index der kleinsten Zahl ist {ermittleIndexDerKleinstenZahl(zahlenliste)}")

print(gibVerdoppelteListeZurueck(zahlenliste))

entferneGeradeZahlen(zahlenliste)
print(zahlenliste)

print(sindAlleZahlenPositiv(zahlenliste))

print(mehrPositiveOderNegativeZahlen(zahlenliste))

print(enthaeltDuplikate(zahlenliste))
