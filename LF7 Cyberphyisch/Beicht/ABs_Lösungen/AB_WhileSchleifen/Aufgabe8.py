breite = int(input("Gib die breite ein."))
hoehe = int(input("Gib die höhe an."))

i = 0
while(i < hoehe):
    if (i == 0 or i == hoehe-1): print("X" * breite)
    else: print("X" + " "*(breite-2) + "X")
    i += 1