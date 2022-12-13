from pymongo import MongoClient

database = MongoClient('mongodb://localhost:27017/')['artikelverwaltung_db']
collection = database['artikel']

schrank_daten = {
    'artikel_nr': '002348',
    'name': 'Holzschrank HS900',
    'hersteller': 'Möbel GmbH',
    'preis': '588.00 Euro'
}
collection.insert_one(schrank_daten)

tisch_daten = {
    'artikel_nr': '1234',
    'name': 'Holztisch HT73',
    'hersteller': 'Möbel GmbH',
    'preis': '213.45 Euro'
}

stuhl_daten = {
    'artikel_nr': '5401',
    'name': 'Holzstuhl HST08',
    'hersteller': 'Möbel GmbH',
    'preis': '43.71 Euro'
}
collection.insert_many(tisch_daten, stuhl_daten)

daten = collection.find_one({"artikel_nr": "1234"})
print("Daten des Artikels mit der Nr. 1234")
print(daten)
print("Alle Artikel des Herstellers -Möbel GmbH-")
for daten in collection.find({"hersteller": "Möbel GmbH"}):
    print(daten)