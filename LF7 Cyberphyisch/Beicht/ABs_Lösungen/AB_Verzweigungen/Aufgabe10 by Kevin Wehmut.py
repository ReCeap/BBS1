#Code von Kevin!

def printGraphInformation():
  print("Bitte gib mir die Parameter für eine Parabelgleichung f(x) = a(x)^2 + bx + c")
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))

  # ÖFFNUNGSRICHTUNG
  print("\n=== Öffnungsrichtung === \n")
  if(a > 0):
    print("Parabel ist nach oben geöffnet")
  elif(a < 0):
    print("Parabel ist nach unten geöffnet")
  else:
    print("Keine quadratische Funktion")
    return

  # STAUCH- BZW. STRECKFAKTOREN
  print("\n=== Stauch- bzw. Streckfaktoren === \n")
  if(a > 1):
    print("Parabel ist gestreckt")
  elif(a < 1):
    print("Parabel ist gestaucht")
  else:
    print("Parabel ist weder gestaucht noch gestreckt")

  # NULLSTELLEN
  print("\n=== Nullstellen === \n")
  q = (b / 2 * a) ** 2 - c / a
  if(q > 0):
    print("Parabel hat 2 Nullstellen")
  elif(q < 0):
    print("Parabel hat keine Nullstellen")
  else:
    print("Parabel hat eine doppelte Nullstelle")

printGraphInformation()
