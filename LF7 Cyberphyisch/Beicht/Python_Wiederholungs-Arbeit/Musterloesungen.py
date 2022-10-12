import math
from pickle import APPEND

def aufgabe1(start, ende):
    return list(range(start, ende+1))

def aufgabe2(laenge, hoehe, kosten, packet):
    wand = laenge * hoehe
    packete = math.ceil(wand / packet)
    return packete*kosten

def aufgabe3(string):
    return string.split("#")

def aufgabe4(string1, string2):
    isIn = []
    for c in string1:
        if c in string2 and c not in isIn: 
            isIn.append(c)
    return len(isIn)

def bonusaufgabe(string):
    added= {}
    for c in string:
        if c in added:
            added[c] += 1
        else:
            added[c] = 1
    return " ".join([str(f"{k}:{v}") for k, v in added.items()])
