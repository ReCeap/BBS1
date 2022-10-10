#Code von Kevin!

import math

# CODE SETZT KORREKTE INPUTS VORAUS, KEIN ERRORHANDLING;

def calcAndPrintZeroPoints():
  print("Bitte gib die Parameter deiner quadratischen Gleichung an.")
  aInput = float(input("a: "))
  bInput = float(input("b: "))
  cInput = float(input("c: "))

  if(aInput == 0):
    print("a darf nicht null sein")
    return

  # Leider habe ich fürs Abi nur die Mitternachtsformel gelernt, weswegen ich diese benutzt habe:
  # MITTERNACHTSFORMEL: x1/2 = -b +- (((b**2) - 4 * a * c) ** 0.5) / 2a

  # Berechne einzelne Cluster u.A. zur Bestimmung von n(Nst) 
  x = bInput ** 2
  y = 4 * aInput * cInput
  z = x - y
  s = z ** 0.5 # hoch 0.5 ist das gleiche wie Quadratwurzel
  numeratorPlus = -bInput + s
  numeratorMinus = -bInput - s
  denominator = 2 * aInput
  nst1 = numeratorPlus / denominator
  nst2 = numeratorMinus / denominator

  if(z < 0):
    print("Es gibt keine Nullstellen")
    return
  elif(s == 0):
    print(f"Doppelte Nullstelle bei ({nst1}|0)")
    return
  else:
    print(f"Die Nullstellen sind ({nst1}|0) und ({nst2}|0)")
    return


calcAndPrintZeroPoints()