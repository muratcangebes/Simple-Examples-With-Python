liste=['a','b','c','d']
deger='a'
if((deger in liste) and (deger==liste[0])):
    print("Listede var ve ilk eleman")
elif deger in liste:
    print("Listede var ancak ilk eleman değil")
else:
    print("Listede yok")
