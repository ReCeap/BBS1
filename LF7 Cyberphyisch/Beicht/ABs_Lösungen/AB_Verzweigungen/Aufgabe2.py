a = int(input("Gib die erste Zahl ein."))
b = int(input("Gib die zweite Zahl ein."))

if (a < 0 or b < 0): print("Error: Eine der Zahlen ist negativ.")
elif (a == 0 or b == 0): print("Error: Man kann nicht durch 0 teilen.")
elif (a > b): print(a/b)
else: print(b/a)