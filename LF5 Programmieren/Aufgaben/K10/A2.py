def sortieren_newlist(liste):
    returnlist=[]
    while len(liste) !=0:
        returnlist.append(min(liste))
        liste.remove(min(liste))
    return returnlist

print(sortieren_newlist([1,7,5,54,7,8,9]))

def umsortierung(liste):
    for i in range(len(liste)):
        for i in range(len(liste)-1):
            if liste[i] > liste[i+1]:
                g=liste[i]
                k=liste[i+1]
                liste[i] = k
                liste[i+1] = g
    return liste

print(umsortierung([1,4,3,2,34,53,564,47,6,37,45,74568,568,5]))