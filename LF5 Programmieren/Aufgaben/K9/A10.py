Frage1 = "Was ist die Hautpstadt von Deutschland?"
Antwort1 = "Berlin"
Frage2 = "Die Hauptstadt von Hessen ist?"
Antwort2 = "Wiesbaden"
Frage3 = "Was ist 20 * 5?"
Antwort3 = "100"

def questions():
    points = 0
    user_Input = input(Frage1)
    if user_Input == Antwort1:
        points += 1
    user_Input = input(Frage2)
    if user_Input == Antwort2:
        points += 1
    user_Input = input(Frage3)
    if user_Input == Antwort3:
        points += 1
    print("Du hast ", points, " von 3 Punkten erreicht!")
    
questions()