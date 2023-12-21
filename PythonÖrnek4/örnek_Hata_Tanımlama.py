# 08.12.2023 --- Örnek


try:
    yas = int(input("Yaşınızı girin : "))

    if(yas < 0):
        raise  ValueError("Sıfırdan Küçük Yaş Olamaz!")
    elif(yas > 35) :
        raise ValueError("35 Yaş Üstü Kayıt Olamaz.")
    elif(yas < 18) :
        raise  ValueError("18 Yaşından Küçükler Kayıt Olamaz.")
    else:
        print("BAŞARILI --- Kayıt Tamamlandı!!")

except ValueError as hata:
    print(hata)

