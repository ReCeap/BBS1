list = [1,4,3,2,34,53,564,47,6,37,45,74568,568,5]

def sortieren_newlist(liste):
    returnlist=[]
    l=liste.copy()
    while len(l) !=0:
        returnlist.append(min(l))
        l.remove(min(l))
    return returnlist

print(sortieren_newlist(list))
print(list)

def umsortierung(liste):
    l=liste.copy()
    for i in range(len(l)):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    return l

print(umsortierung(list))
print(list)