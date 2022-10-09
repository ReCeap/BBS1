#Code von Kevin!

def getGraphPoints():
  print("Bitte gib mir die Parameter für eine lineare Funktion.")
  m = float(input("Steigung: "))
  b = float(input("y-Achsenabschnitt: "))

  print(f"f(x) = {m} * x + {b}")

  print("\nMöchtest du einen x-Wert bestimmen, um den Funktionswert zu berechnen (x) oder einen y-Wert bestimmen, um den x-Wert zu vermitteln (y)? Alternativ kannst du dir mit (n) die Nullstellen ausgeben lassen.")
  operation = input("(x/y/n): ").lower()

  if(operation == "x"):
    x = float(input("Wähle dein x: "))
    return f"Bei f(x) = {m} * {x} + {b} ist\nf(x) = {m * x + b}, also ({x}|{m * x + b})"
  elif(operation == "y"):
    y = float(input("Wähle dein y: "))
    return f"Bei {y} = {m} * x + {b} ist\nx = {(y - b) / m}, also ({(y - b) / m}|{y})"
  elif(operation == "n"):
    nstX = -b / m
    return f"Deine Nullstelle liegt bei ({nstX}|0)"
  else:
    return

print(getGraphPoints())
