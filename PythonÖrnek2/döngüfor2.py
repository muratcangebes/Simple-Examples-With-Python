kisiler=['Ahmet Ak','Ayşe Cengiz','Burak Koç',
         'Ceyda Yaşar','Deniz Kara']
sayi=0
for yazdir in kisiler:
    sayi = sayi+1
    ad, soyad=yazdir.split()[0], yazdir.split()[1]
    print('{0}. kişinin adı {1}, {0}. kişinin soyadı {2}'.format(sayi,ad,soyad))

