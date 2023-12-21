# 08.12.2023 --- try,except,finally --- Örnek

while True:
    sayi = input("Karesi Alınacak Bir Sayı Giriniz = ")


    try:
        sayi = int(sayi)
        sonuc = pow(sayi,2)   # pow --> üs alma , karesini alma

        print(" [ {} ] Sayısının Karesi = {}".format(sayi,sonuc))
        break

    except:
        print("// Girilen değer işleme uygun değil!")


# en üstte while true: yazıp altındaki herseyi şeçip tab tuşuna basarsak içine alır.