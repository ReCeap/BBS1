jahr = int(input("Gib das Jahr an: "))

if (jahr%4 == 0 and (jahr%100 != 0 or jahr%400 == 0)): print("Es ist ein Schaltjahr.")
else: print("Es ist kein Schaltjahr.")