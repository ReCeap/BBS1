import random 

class Krieger:
    def __init__(self):
        self.initiative = random.randrange(1,8)
        self.maxhealthpoints = random.randrange(1,8)
        self.healthpoints = self.maxhealthpoints
        self.heal = random.randrange(1,8)
        self.healleft = True
        
    def attack(self):
        self.attackdmg = random.randrange(1,7)
        print(self.attackdmg)

    def block(self):
        random.randrange(1 ,4)

    def heal(self):
        if self.healleft == True:
            if self.healthpoints == self.maxhealthpoints:
                print("Du kannst nicht heilen!")
            elif (self.heal + self.healthpoints) > self.maxhealthpoints:
                  self.healthpoints = self.maxhealthpoints
                  self.healleft = False
            else:
                  self.healthpoints += self.heal
                  self.healleft = False


        
    
my_krieger = Krieger()
my_krieger.attack()