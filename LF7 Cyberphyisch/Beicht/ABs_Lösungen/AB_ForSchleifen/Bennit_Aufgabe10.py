prime = True
num = int(input("Bitte gib eine natürliche Zahl ein."))
for i in range(2, num):
    if (num%i == 0): 
        prime = False
print(f"{num} ist eine Primzahl." if(prime) else f"{num} ist keine Primzahl!")