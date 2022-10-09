def pyramide(laengeGrundflaechendiagonale, hoehe):
    grundKante = (laengeGrundflaechendiagonale**2/2)
    print(f"Oberfläche: {(grundKante**2) + (2 * grundKante * hoehe)}")
    print(f"Volumen: {1/3 * grundKante**2 * hoehe}")