adjektive = ["rote", "gelbe", "grüne", "blaue", "große", "kleine"]
fruechte = ["Äpfel", "Bananen", "Birnen", "Grapefruits", "Kaktusfeige"]

for a in adjektive:
    for f in fruechte:
        if(len(a) < len(f) and a[0].lower() != f[0].lower()): print(a, f)