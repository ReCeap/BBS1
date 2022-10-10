noten = []
while(True):
    note = input("Gib eine Schulnote an: ")
    if(note.lower() == "ende"): break
    elif (int(note) < 1 or int(note) > 6): 
        print("Keine gültige Schulnote!“")
        continue
    noten.append(int(note))

print(f"Dein Notendurchschnitt ist {sum(noten)/len(noten)}")