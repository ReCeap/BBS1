#Erste Aufgabe
breite = int(input("Gib die breite ein."))
hoehe = int(input("Gib die höhe an."))
for h in range(hoehe):
    print("X"*breite)
    
#Zweite Aufgabe
breite = int(input("Gib die breite ein."))
hoehe = int(input("Gib die höhe an."))
for h in range(hoehe):
    if (h == 0 or h == hoehe-1): print("X"*breite)
    else: print("X" + " "*(breite-2) + "X")