class ucus():
    havayolu="THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons(self):
        return('{} sefer sayılı, {}-{} uçuşumuz {} dakika sürecektir.'
               .format(self.kod, self.kalkis, self.varis, self.sure))

    def satis(self,a):
        if self.yolcu+a<=self.kapasite:
            print("{} bilet satıldı, {} boş koltuk kaldı."
               .format(a,(self.kapasite-self.yolcu-a)))
        else:
            print("Satış için yeterli koltuk yok")

    def iptal(self,adet):
        if self.yolcu>=adet:
            print("{} bilet iptal edildi, güncel koltuk sayısı {}."
                  .format(adet,(self.kapasite-(self.yolcu-adet))))
        else:
            print("İptal için fazla koltuk girildi")

u1=ucus('TK1001','ESK','IZM', 45, 450, 300)
u2=ucus('TK3014','ANK','IST', 55, 375, 315)

print(u2.anons())
u1.satis(200)
u1.iptal(50)



