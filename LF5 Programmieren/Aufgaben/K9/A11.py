import random

#def Kino():
print("-" * 55)
for x in range(0,6):
    if x == 2:
        print("-" * 55)
    a = []
    for y in range(0,9):
        random_num = random.randrange(0, 100)
        if random_num >= 50:
            a.append("X")
        else:
            a.append("-")
    print("Reihe", x + 1 , " ", a)
print("-" * 55)
            
#Kino()

class pkw:
    def __init__(self, motor, türen):
        self.motor = motor
        self.tür= türen
        
audi = pkw("100ps", 5)
porsche = pkw("500ps", 3)

porsche.motor = "700ps"

print(porsche.motor)