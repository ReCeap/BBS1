import math

def wuerfel(kantenlaenge):
    print(f"Oberfläche: {kantenlaenge**2}")
    print(f"Volumen: {kantenlaenge**3}")
    
def quader(laenge, hohe, breite):
    print(f"Oberfläche: {laenge*breite}")
    print(f"Volumen: {laenge*hohe*breite}")
    
def kugel(radius):
    print(f"Oberfläche: {4*math.pi*radius**2}")
    print(f"Volumen: {4/3*math.pi*radius**3}")