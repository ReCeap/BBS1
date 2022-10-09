f = int(input("Wie viele fahrten planen sie?: "))
gp = 5
ob = f * gp
zb = f * (gp * 0.75) + 50
fb = f * (gp * 0.5) + 200

print(f"Ohne Bahncard: {ob}€")
print(f"Bahncard25: {zb}€")
print(f"Bahncard50: {fb}€")

if (min([ob, zb, fb]) == fb): print(f"Für die gewählten {f} Fahrten ist der Kauf einer Bahncard 50 sinnvoll.")
elif (min([ob, zb, fb]) == zb): print(f"Für die gewählten {f} Fahrten ist der Kauf einer Bahncard 25 sinnvoll.")
elif (min([ob, zb, fb]) == ob): print(f"Für die gewählten {f} Fahrten ist weder der Kauf einer Bahncard 50 noch einer Bahncard 25 sinnvoll.")