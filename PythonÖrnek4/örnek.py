# 08.12.2023 --- Hata Durumlarını Analiz Edip Bölme İşlemi


try:
    sayi1 = int(input("Birinci Sayıyı Girin = "))
    sayi2 = int(input("İkinci Sayıyı Girin = "))
except ValueError:
    print("// BU ALANA SADECE SAYI GİRİN //")

else:
    try:
        print(sayi1/sayi2)
    except ZeroDivisionError:
        print("// Sıfıra Bölme Hatası! //")









