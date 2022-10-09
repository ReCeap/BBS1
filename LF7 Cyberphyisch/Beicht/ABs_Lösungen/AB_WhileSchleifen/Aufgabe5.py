import random

meineZufallszahl = random.randint(0,100)

while(True):
    tip = int(input("Rate eine Zahl: "))
    if (tip < 0): break
    elif (tip < meineZufallszahl): print("Dein Tipp ist zu klein.")
    elif (tip > meineZufallszahl): print("Dein Tipp ist zu groß.")
    elif (tip == meineZufallszahl): 
        print("GG WP!")
        break
    