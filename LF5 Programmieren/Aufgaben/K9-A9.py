random_Num = input("Gib dem Script eine Zahl zum Raten.")
random_Num = int(random_Num)

num_Cracked = False

def raten():
    zahl = 0
    while(num_Cracked == False):
        if zahl == random_Num:
            print("Der Script hat die Zahl erraten. Es war: ", zahl)
            break
        zahl += 1
        print("Ich rate:", zahl)
        
raten()