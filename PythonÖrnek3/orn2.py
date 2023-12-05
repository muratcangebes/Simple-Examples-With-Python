# and (ve): koşulların tamamı sağlanıyorsa doğru kabul eder
# or (yada): koşullardan herhangi birisi doğru olduğu durumda doğru kabul eder

liste=['a','b','c','d']
deger='f'
if(deger in liste):
    print("Listede var")
    if(deger==liste[0]):
        print("Listenin ilk elemanı")
    else:
        print("Listenin ilk elemanı değil")
else:
    print("Listede yok")
    liste.append(deger)
    print("Listeye ekledim. Listenin son hali {}"
          .format(liste))
