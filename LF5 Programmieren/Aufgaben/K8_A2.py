int1 = 9
int2 = 17
int3 = 15

list = []

#Switch case 1
if int1 > int2 and int2 > int3:
    print(int3, " ", int2, " ", int1)

#Switch case 2 
elif int1 > int2 and int2 < int3:
    print(int2, " ", int3, " ", int1)

#Switch case 3
elif int1 < int2 and int3 < int1:
    print(int3, " ", int1, " ", int2)

#Switch case 4   
elif int1 < int2 and int3 > int1:
    print(int1, " ", int3, " ", int2)

#Switch case 5    
elif int1 > int2 and int1 < int3:
    print(int2, " ", int1, " ", int3)

#Switch case 6   
elif int1 < int2 and int2 < int3:
    print(int1, " ", int2, " ", int3)
    
else:
    print("Error#001: Min. zwei Zahlen haben den Selben wert!")



list.append(int1)
list.append(int2)
list.append(int3)
list.sort()
print(list)