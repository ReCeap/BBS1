# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:12:29 2021

@author: Christian
"""

"""
↑↑↑↑  ↑↑↑↑

↓↓↓↓  ↓↓↓↓
"""


###---------------------------------------------------------------------------------------------------------------------------------------###
"""
IF_ELSE Abfragen
"""

friend = "Rolf"
user_name=input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
    print("This runs too.")
    
print("This runs anyway.")

friend = "Rolf"
user_name=input("Enter your name: ")

if user_name == friend:
    print("Hello, friend!")
else:
    print("Hello, stranger!")
    
    
name = input("Enter your name: ")

print(bool(name))

if name:
    print("We know your name.")


friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")


if user_name in friends:
    print("Hello, friend!")
if user_name in family:
    print("Hello, family")
else:
    print("I don't know you.")
    
"""
↑↑↑↑ Schlecht da das letzte "ELSE Statement" ausgeführt wird auch wenn das erste "IF Statement" korrekt ist, da die beiden Funktionen nicht mit einander verankert sind. ↑↑↑↑

↓↓↓↓ Um das zu verhindern wird die Funktion "ELIF" verwendet. ↓↓↓↓
"""

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name: ")


if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family")
else:
    print("I don't know you.")
    
###---------------------------------------------------------------------------------------------------------------------------------------###
"""
WHILE LOOPS
"""
is_learning = True

while is_learning:
    print("You are learning!")
"""
↑↑↑↑ Endlosschleife
"""    

is_learning = True

while is_learning:
    print("You are learning!")
    user_input = input("Are you still leaning?")  
    is_learning = user_input == "yes"



user_input = input("Do you wish to run the program? (yes/no): ")

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you wish to run the program? (yes/no): ")
    
print("We stopped running.")


###---------------------------------------------------------------------------------------------------------------------------------------###
"""
FOR LOOPS
"""

friends = ["Rolf", "Jen", "Anne"]

for friend in friends:
    print(friend)
    
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for index in elements:
    print("Hello, world!")
    
for index in range(0, 1000):
    print(index)
    
students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},
    ]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")
###---------------------------------------------------------------------------------------------------------------------------------------###
"""
DESTRUCTURING SYNTAX
"""
currencies = 0.8, 1.2 
usd, eur = currencies #0.8 wird dem "USD" zugeteilt und 1.2 wird "EUR" zugeteilt



friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob",22)]


for friend in friends:
    print(friend)
    
"""
('Rolf', 25)
('Anne', 37)
('Charlie', 31)
('Bob', 22)
↑↑↑↑ Output ist hässlich. ↑↑↑↑


↓↓↓↓ Besser ↓↓↓↓
Rolf 25
Anne 37
Charlie 31
Bob 22
"""

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob",22)]


for name, age in friends:
    print(name, age)

"""
↑↑↑↑ Besser ↑↑↑↑


↓↓↓↓ Am besten ↓↓↓↓
Rolf is 25 years old.
Anne is 37 years old.
Charlie is 31 years old.
Bob is 22 years old.
"""

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob",22)]


for name, age in friends:
    print(f"{name} is {age} years old.")

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
ITERATING OVER DICTIONARIES
"""

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)
"""
↑↑↑↑ Gibt die "KEY_values" wieder. ↑↑↑↑

↓↓↓↓ ".VALUES" Gibt die Werte der zu den key_values wieder. ↓↓↓↓
"""

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for age in friend_ages.values():
    print(age)

"""
↓↓↓↓ ".ITEMS" Gibt die "KEY_values" sowie die mit den key_value verbundenen"Werte" wieder. ↓↓↓↓
"""

friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
BREAK and CONTINUE (loops)
"""

cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok",]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
    
"""
↑↑↑↑ "BREAK" unterbricht die Schleife komplett sie wird nicht mehr ausgeführt. ↑↑↑↑

↓↓↓↓ "CONTINUE" überspringt den Sonderfall und führt die Schleife weiter fort. ↓↓↓↓
"""
    
cars = ["ok", "ok", "ok", "ok", "faulty", "ok", "ok",]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skippin...")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")


###---------------------------------------------------------------------------------------------------------------------------------------###
"""
FizzBuzz
"""
number = 1

while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    number += 1
    
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
###---------------------------------------------------------------------------------------------------------------------------------------###
"""
ELSE keyword
"""



cars = ["ok", "ok", "ok", "faulty", "ok", "ok",]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skippin...")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")
"""
Ein "ELSE" nach einer Schleife wird durchgeführt solange kein "BRAKE" in der Schleife aufgetreten ist.
"""

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
FOR LOOPS 2 (Primzahlen mit einer "for loop" finden)
"""

for n in range(2, 100000):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number.")

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
LIST SLICING
"""

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

print(friends[2:4])
print(friends[1:])
print(friends[:4])
print(friends[-3:])
print(friends[-3:4])
print(friends[1:-2])

###---------------------------------------------------------------------------------------------------------------------------------------###
"""
LIST COMPREHENSION
"""

numbers = [0, 1, 2, 3, 4]
double_numbers = []
for number in numbers:
    double_numbers.append(number * 2)
print(double_numbers)


numbers = [0, 1, 2, 3, 4]
double_numbers = []
double_numbers = [number * 2 for number in numbers]
print(double_numbers)

double_numbers = [number * 2 for number in range(5)]
print(double_numbers)



friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]
print(age_strings)



names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


friend = input("Enter you friend name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")


###---------------------------------------------------------------------------------------------------------------------------------------###

###---------------------------------------------------------------------------------------------------------------------------------------###

###---------------------------------------------------------------------------------------------------------------------------------------###

###---------------------------------------------------------------------------------------------------------------------------------------###

###---------------------------------------------------------------------------------------------------------------------------------------###