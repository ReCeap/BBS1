a = int(input("Gib die erste Zahl ein."))
b = int(input("Gib die zweite Zahl ein."))
c = int(input("Gib die dritte Zahl ein."))

#[print(i) for i in sorted([a, b, c])]

if (a < b and a < c and b < c): print(a, b, c)
elif (a < b and a < c and b > c): print(a, c, b)
elif (b < a and b < c and a < c): print(b, a, c)
elif (b < a and b < c and a > c): print(b, c, a)
elif (c < a and c < b and a < b): print(c, a, b)
elif (c < a and c < c and a > b): print(c, b, a)