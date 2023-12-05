liste=[1,2,3,4,5,6]
deger=30
if deger in liste:
    print("Dizide ekli")
else:
    print("Dizide yok")
    liste.append(deger)
    print("Listeye ekledim. Son hali {}"
          .format(liste))
