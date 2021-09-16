# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:55:41 2021

@author: Christian
"""

###---------------------------------------------------------------------------------------------------------------------------------------###

"""
Variablen
"""

age=30
PI=3.14159 

#kleinschreibung für Variablen die geändert werden können GROßSCHREIBUNG für Variablen welche gleich bleiben sollen

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
Mathematik
"""

age = 35 #integer Zahl
PI = 3.14159 #float Zahl

math_operation = 1 + 3 * 4 / 2 - 2
print(math_operation)

float_division = 12/3
print(float_division)

integer_division = 12//3
print(integer_division)

float_division = 8/3
print(float_division)

integer_division = 8//3 #// gibt nur die Zahl vor dem Komma an. Es wird nicht korrekt gerundet 2.6 ergibt 2
print(integer_division)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
Mathematik
"""

integer_division= 13//5
print(integer_division)

rest = 13 % 5
print(rest)

#10 / 2
#14 / 2
#6 / 2
#340 / 2
#Bei graden Zahlen rest=0

#11/2
#27/2
#3/2
#Bei ungraden Zahlen rest=1


x=37
rest = x % 2
print(rest)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
Strings
"""

my_string = "Hello, World!"
print(my_string)


multiline_string = """Hello, world.

Welcome to my Program
"""
print(multiline_string)

age = 34
age_as_string = str(34)
print("You are " + age_as_string)
print(f"You are {age}")

name = "Christian"
greeting = f"How are you, {name}?"

"""
Zahlen können nicht direkt in einen String eingebunden werden.
Um eine Zahl einzubinden muss str() verwendet werden oder ein f_string
"""

name = "Christian"
final_greeting = "How are you, {}"
christian_greeting = final_greeting.format(name)
print(christian_greeting)

name="Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
USER INPUT
"""

my_name = "Christian"
your_name = input("Enter your name?: ")

print(f"Hello {your_name}. My name is {my_name}.")

age = input("Enter your age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")

age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")

age = input("Enter your age: ")
print(f"You have lived for {int(age) * 12} months.")

age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
Booleans
"""

truthy = True
falsy = False

age = 20
is_over_age = age >= 18 #TRUE
is_under_age = age < 18 #FALSE
is_twenty = age == 20   #TRUE



my_number = 5
user_number = int(input("Enter a number: "))

matches = my_number == user_number

print(f"You got it right: {matches}")


###---------------------------------------------------------------------------------------------------------------------------------------###
"""
Boolean: AND & OR
"""

age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}.")


age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65

print(f"At {age}, you are usually not working: {usually_not_working}")
#Schlecht da doppeltes negativ

#Besser zu lesen
age = int(input("Enter your age: "))
usually_working = age >= 18 and age <= 65

print(f"At {age}, you are usually working: {usually_working}")


x = 35 and 0 #"and" gibt den ersten Wert wieder wenn dieser "False" ist und gibt den zweiten Wert wieder wenn der erste Wert "True" ist
print(x)

x =35 or 0 #"or" gibt den ersten Wert wieder wenn dieser "True" ist und gibt den zweiten Wert wieder wenn der erste Wert "False" ist
print(x)

#Anwendung "or"

name = ""
surname = "Smith"

greeting = name or f"Mr. {surname}" #Da "name" leer ist und "False" wiedergibt wirt der zweite Wert verwendet.
print(greeting)

name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}" 
print(greeting)
###---------------------------------------------------------------------------------------------------------------------------------------###
"""
LISTS
"""
#In Listen lassen sich viele Variablen speichern

friends = ["Rolf", "Bob", "Anne"]

print(friends[0])
#Zugriff auf einen Eintrag in der Liste


friends = ["Rolf", "Bob", "Anne"]

print(len(friends))
#Zählt auf wie viele Einträge in der Liste vorhanden sind


#Es lassen sich ebenfalls "Listen" in "Listen" verpacken
friends = [["Rolfs", 24],["Bob", 35],["Anne", 17]]
print(friends[0][0]) #greift auf den ersten eintrag in der ersten verpackten Liste zu


#Hinzugügen von Werten zu einer Liste
friends = ["Rolf", "Bob", "Anne"]
friends.append("Jen")
print(friends)


#Entfernen von Werten aus einer Liste
friends = ["Rolf", "Bob", "Anne"]
friends.remove(friends("Bob"))
print(friends)

friends = [["Rolf", 24],["Bob", 35],["Anne", 17]]
friends.remove(friends(["Anne", 17]))
print(friends)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
LISTS_2
"""
#"Join" Funktion für Listen

friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")


friends = ["Rolf", "Anne", "Charlie"]
comma_seperated = ", ".join(friends)
print(f"My friends are {comma_seperated}.")


###---------------------------------------------------------------------------------------------------------------------------------------###
"""
TUPELS
"""
#Ähnlich einer "Liste" Werte können jedoch nicht angepasst werden.

short_tuple = "Rolf", "Bob"
a_bit_clearer = ("Rolf", "Bob")#Klammern machen deutlich, dass es sich um einen "Tupel" handelt und müssen verwendet werden, wenn der Tupel in eine Liste eingebunden werden soll
"""
tupel_in_list = ["Rolf", "Bob"] #FALSCH
tupel_in_list = [("Rolf", "Bob")] #Richtig
"""

friends = ("Rolf", "Bob", "Anne")
friends.append("Jen") #append funktioniert nicht bei "tuples"


friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)
print(friends) 

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
SETS
"""
#"Sets" können kein duplikate enthalten und halten sich nicht die Reihenfolge der Werte
#"Sets" bieten sich an um sehr einfach vergleiche zueinander durchzuführen

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
print(art_friends)

art_friends.remove("Jen")
print(art_friends)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
SETS_2
"""

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
print(art_but_not_science)
print(science_but_not_art)


art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}
all_friends = art_friends.union(science_friends)
print(all_friends)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
DICTIONARIES
"""
#"Dictionaries" enthalten informationen zu bestimmten "Key wörtern"
#Das "Key wort" ist in Anführungszeichen und wird von dem dazugehörigen wert gefolgt 

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 25}
print("Rolf ist",friend_ages["Rolf"])


friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 25}
#Hinzufügen von Werten zu eine "Dictionarie"
friend_ages["Bob"] = 20

#Anpassen eines Wertes in einem "Dictionarie"
friend_ages["Rolf"] = 27
print(friend_ages)

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 17},
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])



friends = [("Rolf", 24),("Bob", 35),("Anne", 17)]
friend_ages = dict(friends)
print(friend_ages)

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
LENGTH and SUM
"""

grades = [80, 75, 90, 100]

total = sum(grades) #"sum" summiert die Werte einer Liste
length = len(grades) #"len" zählt die Werte einer Liste

average = total / length
print(average)


###---------------------------------------------------------------------------------------------------------------------------------------###

###---------------------------------------------------------------------------------------------------------------------------------------###
