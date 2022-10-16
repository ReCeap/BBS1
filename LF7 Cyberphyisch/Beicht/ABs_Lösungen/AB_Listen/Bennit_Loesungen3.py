#Aufgabe 1a
print([i for i in range(10, 100) if i%2==0])

#Aufgabe 1b
print([i for i in range(-50, 51) if i%2==0 and i%3==0])

#Aufgabe 1c
print([i**2 for i in range(-9, 10)])

#Aufgabe 1d
print([2*i**2-(4*i)+6 for i in range(-5, 6)])

#Aufgabe 2a
liste = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]

#Aufgabe 2b
liste = []
for i in range(4):
    row = []
    for it in range(4):
        row.append(it+i)
    liste.append(row)
print(liste)

#Aufgabe 2c
print([[i+it for it in range(4)] for i in range(4)])

#Aufgabe 2d
print([[i, i+1, i+2, i+3] for i in range(4)])

#Aufgabe 3a
def erstelleSpielkonstellationen(spielerzahl):
    liste = []
    for i in range(1, spielerzahl+1):
        for it in range(i+1, spielerzahl+1):
            liste.append([i, it])
    return liste

#Aufgabe 3b Unfertig
def erstelleSpielkonstellationen(spielerzahl):
    liste = []
    for i in range(1, spielerzahl+1):
        pass