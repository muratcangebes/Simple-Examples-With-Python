# 08.12.2023 --- try,except,finally


sayi = input("Ondalıklı sayı giriniz = ")
mesaj = ""

try:
    sayi = float(sayi)
    print("YUVARLANMIŞ HALİ = {}".format(round(sayi)))
    mesaj = "Başarılı"

except:
    print("{} Girdisi yuvarlama işlemine uygun değildir."
          .format(sayi))
    mesaj = "Başarısız"

finally:
    print("Sayı yuvarlama işlemi [ {} ] olarak tamamlandı."
          .format(mesaj))