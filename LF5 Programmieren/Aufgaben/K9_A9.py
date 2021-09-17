random_Num = input("Gib dem Script eine Zahl zum Raten. Zwischen 0 und 100: ")
random_Num = int(random_Num)

range = [-1, 101]

def raten():
    zahl = 50
    tries = 1
    while(True):
        print("Ich rate:", zahl)
        if zahl == random_Num:
            print("Der Script hat die Zahl erraten. Es war: ", zahl)
            break
        elif zahl < random_Num:
            range[0] = zahl
            zahl = round(sum(range) / 2)
        elif zahl > random_Num:
            range[1] = zahl
            zahl = round(sum(range)  / 2)
        tries += 1
    print(f"Ich habe {tries} versuche gebraucht!")
        
raten()