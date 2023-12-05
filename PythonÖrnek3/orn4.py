isim=input("İsminiz: ")
yas=int(input("Yaşınız: "))
ed=input("Mezuniyet: ")
if(yas>=18):
    if(ed=='lise' or ed=='yüksek'):
        print("Ehliyet alabilir")
    else:
        print("Ehliyet alamaz")
else:
    print("Ehliyet alamaz")
