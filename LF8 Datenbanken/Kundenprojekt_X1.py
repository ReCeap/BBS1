import mysql.connector
import datetime

dbconfig = {
  "host": "onlyfranz.de",
  "user": "schuladmin",
  "password": "schulpassword123",
  "database": "Lf8_x1",
  "autocommit": True
}

mydb = mysql.connector.connect(**dbconfig)

#    _____ _   _ _____ _______   _____  ____  
#   |_   _| \ | |_   _|__   __| |  __ \|  _ \ 
#     | | |  \| | | |    | |    | |  | | |_) |
#     | | | . ` | | |    | |    | |  | |  _ < 
#    _| |_| |\  |_| |_   | |    | |__| | |_) |
#   |_____|_| \_|_____|  |_|    |_____/|____/ 

def init_db():
  #Make sure to reconnect to the database and refresh it
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()
  
  #Create Table Abteilung
  cursor.execute("CREATE TABLE IF NOT EXISTS `Abteilungen` (`AbteilungsID` INT NOT NULL AUTO_INCREMENT, `AbteilungsName` TEXT(255) NOT NULL, `Gebühren` FLOAT NOT NULL, PRIMARY KEY (`AbteilungsID`));")

  #Create Table eingeschrieben
  cursor.execute("CREATE TABLE IF NOT EXISTS `eingeschrieben` (`AbteilungsID` INT NOT NULL, `UserID` INT NOT NULL);")
  
  #Create Table Mitglied
  cursor.execute("CREATE TABLE IF NOT EXISTS `Mitglied` (`UserID` INT NOT NULL AUTO_INCREMENT,`Geburtstag` DATE NOT NULL,`Vorname` TEXT NOT NULL,`Nachname` TEXT NOT NULL,PRIMARY KEY (`UserID`));")

  #Create Table Teilnahme
  cursor.execute("CREATE TABLE IF NOT EXISTS `Teilnahme` (`TeilnahmeID` INT NOT NULL AUTO_INCREMENT,`UserID` INT NOT NULL,`Datum` DATE NOT NULL,PRIMARY KEY (`TeilnahmeID`));")
  
  mydb.commit()

#    ______          _       _ _            
#   |  ____|        | |     | | |           
#   | |__   _ __ ___| |_ ___| | | ___ _ __  
#   |  __| | '__/ __| __/ _ \ | |/ _ \ '_ \ 
#   | |____| |  \__ \ ||  __/ | |  __/ | | |
#   |______|_|  |___/\__\___|_|_|\___|_| |_|

def create_mitglied(geburtstag: datetime, name):
  #Make sure to reconnect to the database and refresh it
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()
  
  #Get the next UserID from AUTO_INCREMENT
  cursor.execute("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_NAME = 'Mitglied'")
  mitgliedsID = cursor.fetchone()

  #Create a new Mitglied in the database
  sql = "INSERT INTO `Mitglied` (`Geburtstag`, `Name`) VALUES (%s, %s)"
  values = [geburtstag, name]
  
  #Executes the sql querie with the given values
  cursor.execute(sql, values)
  mydb.commit()
  
  return mitgliedsID

def create_teilnahme(UserID, datum):
  #Make sure to reconnect to the database and refresh it
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()
  
  #Create a new Teilnahme in the database
  sql = "INSERT INTO `Teilnahme` (`UserID`, `Datum`) VALUES (%s, %s)"
  values = [UserID, datum]
  
  #Executes the sql querie with the given values
  cursor.execute(sql, values)
  mydb.commit()
  
def create_abteilung(name, gebuehren):   
  #Make sure to reconnect to the database and refresh it
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()
  
  #Get the next AbteilungsID from AUTO_INCREMENT
  cursor.execute("SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_NAME = 'Abteilungen'")
  abteilungsID = cursor.fetchone()
  
  #Create a new Abteilungen in the database
  sql = "INSERT INTO `Abteilungen` (`Name`, `Gebühren`) VALUES (%s, %s)"
  values = [name, gebuehren]
  
  #Executes the sql querie with the given values
  cursor.execute(sql, values)
  mydb.commit()
  
  return abteilungsID

#    _    _ _                  __ _   _                  
#   | |  | (_)                / _(_) (_)                 
#   | |__| |_ _ __  _____   _| |_ _   _  __ _  ___ _ __  
#   |  __  | | '_ \|_  / | | |  _| | | |/ _` |/ _ \ '_ \ 
#   | |  | | | | | |/ /| |_| | | | |_| | (_| |  __/ | | |
#   |_|  |_|_|_| |_/___|\__,_|_|  \__,_|\__, |\___|_| |_|
#                                        __/ |           
#                                       |___/            
  
def add_mitglied_to_abteilung(UserID, AbteilungsID):
  #Make sure to reconnect to the database and refresh it
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()
  
  #Add a user to an abteilung
  sql = "INSERT INTO `eingeschrieben` (`UserID`, `AbteilungsID`) VALUES (%s, %s)"
  values = [UserID, AbteilungsID]
  
  #Executes the sql querie with the given values
  cursor.execute(sql, values)
  mydb.commit()
    
#             _                 __           
#       /\   | |               / _|          
#      /  \  | |__  _ __ _   _| |_ ___ _ __  
#     / /\ \ | '_ \| '__| | | |  _/ _ \ '_ \ 
#    / ____ \| |_) | |  | |_| | ||  __/ | | |
#   /_/    \_\_.__/|_|   \__,_|_| \___|_| |_|

#    _    _ _   _ _ 
#   | |  | | | (_) |
#   | |  | | |_ _| |
#   | |  | | __| | |
#   | |__| | |_| | |
#    \____/ \__|_|_|

def check_for_geburtstag():
  mydb.reconnect()
  cursor = mydb.cursor()
  mydb.commit()

  sql = "SELECT `Name`, `Geburtstag` FROM `Mitglied` WHERE Geburtstag = %s"
  values = [datetime.date.today()]
  cursor.execute(sql, values)
  geburtstage = cursor.fetchall()
  
  for user_tupel in geburtstage:
    print(f"{user_tupel[0]} hat heute Geburtstag!")
    
check_for_geburtstag()
while(True):
  user_input = input("Bitte wählen sie ein aktion aus.\n\n")
  
  #    ______          _       _ _            
  #   |  ____|        | |     | | |           
  #   | |__   _ __ ___| |_ ___| | | ___ _ __  
  #   |  __| | '__/ __| __/ _ \ | |/ _ \ '_ \ 
  #   | |____| |  \__ \ ||  __/ | |  __/ | | |
  #   |______|_|  |___/\__\___|_|_|\___|_| |_|
  
  if (user_input.lower() in ["mitglied_erstellen", "mitglied erstellen", "me", "neues_mitglied", "neues mitglied", "nm"]):
    name = input("Bitte gib den Namen des Mitglieds an.")
    geburtstagstr = input(f"Wann hat {name} Geburtstag?")
    geburtstag = datetime.date(geburtstagstr)
    userID = create_mitglied(geburtstag, name)
    print(f"{name} wurde in der Datenbank mit der {userID} hinterlegt.\n")
    
  elif (user_input.lower() in ["teilnahme_erstellen", "teilnahme erstellen", "te", "neue_teilnahme", "neue teilnahme", "nt"]):
    userID = input("Bitte gib die UserID des Mitglieds an.")
    datum = input("Wann hat das Mitglied am Training teilgenommen?")
    create_teilnahme(userID, datum)
    print("Die Teilnahme wurde in der Datenbank hinterlegt.\n")
    
  elif (user_input.lower() in ["abteilung_erstellen", "abteilung erstellen", "ae", "neue_abteilung", "neue abteilung", "na"]):
    name = input("Bitte gib den Namen der neuen Abteilung an.")
    gebuehren = input("Wie hoch sind die Gebühren der Abteilung?")
    abteilungsID = create_abteilung(name, gebuehren)
    print(f"Die Abteilung {name} wurde mit der {abteilungsID} erstellt.\n")
    
  #    _    _ _                  __ _   _                  
  #   | |  | (_)                / _(_) (_)                 
  #   | |__| |_ _ __  _____   _| |_ _   _  __ _  ___ _ __  
  #   |  __  | | '_ \|_  / | | |  _| | | |/ _` |/ _ \ '_ \ 
  #   | |  | | | | | |/ /| |_| | | | |_| | (_| |  __/ | | |
  #   |_|  |_|_|_| |_/___|\__,_|_|  \__,_|\__, |\___|_| |_|
  #                                        __/ |           
  #                                       |___/            
    
  elif (user_input.lower() in ["mitglied_zu_abteilung", "mitglied zu abteilung", "mitglied abteilung", "ma", "mza", "mitglied_zu_abteilung", "eingeschrieben", "einschreiben"]):
    userID = input("Bitte gib die UserID des Mitglieds an welches du einer Abteilung zuweisen möchtest.")
    abteilungsID = input("Bitte gib die AbteilungsID ein.")
    add_mitglied_to_abteilung(userID, abteilungsID)
    print("Das Mitglied wurde der Abteilung hinzugefügt.\n")
    
  #             _                 __           
  #       /\   | |               / _|          
  #      /  \  | |__  _ __ _   _| |_ ___ _ __  
  #     / /\ \ | '_ \| '__| | | |  _/ _ \ '_ \ 
  #    / ____ \| |_) | |  | |_| | ||  __/ | | |
  #   /_/    \_\_.__/|_|   \__,_|_| \___|_| |_|
  
  #    _    _      _       
  #   | |  | |    | |      
  #   | |__| | ___| |_ __  
  #   |  __  |/ _ \ | '_ \ 
  #   | |  | |  __/ | |_) |
  #   |_|  |_|\___|_| .__/ 
  #                 |_|    
    
  else:
    print("Das ist kein gültiger Befehl.\n")
    print("Du hast folgende möglichkeiten:\n")
    
    print("Erstellen:\n")
    print("Mitglied erstellen(me): Erstellt ein neues Mitglied in der Datenbank. Parameter: Name | Geburtsdatum\n")
    print("Teilnahme erstellen(te): Erstellt eine neue Teilnahme in der Datenbank. Parameter: UserID | Datum\n")
    print("Abteilung erstellen(ae): Erstellt ein neue Abteilung in der Datenbank. Parameter: Name | Gebühren\n")
    
    print("Hinzufügen:\n")
    print("Einschreiben: Schreibt ein Mitglied in eine Abteilung ein. Parameter: UserID | AbteilungsID\n")
    
    print("Abrufen:\n")
    print("Alle Mitglieder(am): Gibts alle Mitglieder aus. Optionale Parameter: AbteilungsID | Geburtsdatum\n")
    print("Alle Teilnahmen(at): Gibts alle Teilnahmen aus. Optionale Parameter: UserID | Datum\n")
