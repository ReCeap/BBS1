while(True):
    b = input("Gib mir ein Bundesland: ").lower()
    if (b in ["baden-württemberg", "baden-wuerttemberg", "baden württemberg", "baden wuerttemberg"]): print("Stuttgart")
    elif (b == "bayern"): print("München")
    elif (b == "berlin"): print("Berlin")
    elif (b == "brandenburg"): print("Potsdam")
    elif (b == "hamburg"): print("Hamburg")
    elif (b == "hessen"): print("Wiesbaden")
    elif (b in ["mecklenburg-vorpommern", "mecklenburg vorpommern"]): print("Schwerin")
    elif (b == "niedersachsen"): print("Hannover")
    elif (b in ["nordrhein-westfalen", "nordrhein westfalen"]): print("Düsseldorf")
    elif (b in ["rheinland-pfalz", "rheinland pfalz"]): print("Mainz")
    elif (b == "saarland"): print("Saarbrücken")
    elif (b == "sachsen"): print("Dresden")
    elif (b in ["sachsen-anhalt", "sachsen anhalt"]): print("Magdeburg")
    elif (b in ["schleswig-holstein", "schleswig holstein"]): print("Kiel")
    elif (b in ["thüringen", "thueringen"]): print("Erfurt")
    elif (b == "ende"): break
    else: print("Falsche Eingabe")
    