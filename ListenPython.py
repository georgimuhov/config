'''
liste = ["a","b","c","d","e"]

#print(liste[2])
#For Each-Schleife
for i in liste:
    print(i)
'''

anzahl_ = 25
i = 0
j = 1
r = 1
while i < anzahl_:
    print(j, end=" ")
    j = j + r
    if j == 5: r = -1
    if j == 1: r = 1
    i = i + 1
