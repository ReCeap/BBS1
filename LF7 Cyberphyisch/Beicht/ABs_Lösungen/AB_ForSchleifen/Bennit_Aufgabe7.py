summe = 0
for i in range(1, int(input("Bitte gib eine natürliche Zahl ein."))+1):
    if(i%2 == 0):
        summe += i
print(summe)
        
print(sum([i for i in range(1, int(input("Bitte gib eine natürliche Zahl ein."))+1) if i%2 == 0]))