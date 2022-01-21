sort_me = [1,4,19,243,2,49,67,7,6]

def sort(liste):
    temp = []
    for i in range(len(liste)):
        temp.append(liste.pop(liste.index(min(liste))))
    return temp

print(sort(sort_me))