a = int(input("Gib die erste Zahl ein."))
b = int(input("Gib die zweite Zahl ein."))

i = int(input("Was soll gemacht werden?"))

if (i == 1): print(a+b)
elif (i == 2): print(a-b)
elif (i == 3): print(a*b)
elif (i == 4): print(a/b)
elif (i == 5): print(a//b)
elif (i == 6): print(a%b)
elif (i == 7): print(a**b)
else: print("Keine gültige Option. (Optionen sind 1-7)")