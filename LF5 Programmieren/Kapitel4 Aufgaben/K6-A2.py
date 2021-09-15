if __name__ == "__main__":
    
    def spritkosten(kilometer, verbrauch, preis_Liter):
        return (((verbrauch/100)*kilometer)*preis_Liter)

    print(round(spritkosten(30, 6, 1.36),2), "€")

"""
Laufende Kosten werden hier nicht mit einberechnet.
Es fehlen zum Beispiel Versicherungskosten, Wertverlust, Verschleiß oder auch Steuern.
"""