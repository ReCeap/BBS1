import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
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

  sql = "SELECT `Name`, `Geburtstag` FROM `Mitglied` WHERE Geburtstag = %s"
  values = [datetime.date.today()]
  cursor.execute(sql, values)
  geburtstage = cursor.fetchall()
  
  for user_tupel in geburtstage:
    print(f"{user_tupel[0]} hat heute Geburtstag!")
    
#    _  _________      ____     __
#   | |/ /_   _\ \    / /\ \   / /
#   | ' /  | |  \ \  / /  \ \_/ / 
#   |  <   | |   \ \/ /    \   /  
#   | . \ _| |_   \  /      | |   
#   |_|\_\_____|   \/       |_|   

class MainLayout(BoxLayout):
    pass

class ProjektApp(App):
    def build(self):
        pass
    
if __name__ == "__main__":
    ProjektApp().run()