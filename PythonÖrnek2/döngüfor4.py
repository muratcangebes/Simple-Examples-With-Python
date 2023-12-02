kisiler=['Ahmet Ak','Ayşe Cengiz','Faruk Can','Burak Koç','Ceyda Yaşar','Deniz Kara']

ayrilan='Faruk Can'
sayi=0
asayi=0
for yazdir in kisiler:
    ad, soyad=yazdir.split()[0], yazdir.split()[1]
    if(yazdir==ayrilan):
        asayi=asayi+1
        print('{0}. Ayrılan kişinin adı {1}, Soyadı {2}'
              .format(asayi, ad, soyad))
    else:
        sayi=sayi+1
        print('{0}. Kişinin adı {1}, Soyadı {2}'
              .format(sayi, ad, soyad))
