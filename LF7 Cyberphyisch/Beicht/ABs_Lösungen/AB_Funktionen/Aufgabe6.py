def berechneAnzahlReiskoernerAufFeldA(n):
    if n == 1: return 1
    return 2**(n-1)

def berechneAnzahlReiskoernerAufFeldB(n):
    sum = 1
    for i in range(1, n):
        sum *= 2
    return sum