# 08.12.2023 --- Class Yapısı__2

class ucus():
    havayolu = "THY"

    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anons(self):
        return ('[ {} ] Sefer Sayılı,  ( {} --> {} ) Uçuşunuz {} dakika sürecektir.'
                .format(self.kod,self.kalkis,self.varis,self.sure,))

    def satis(self,a):
        return ("{} Bilet Satıldı, {} Tane Boş Koltuk Kaldı."
                .format(a,(self.kapasite-self.yolcu-a)))


u1 = ucus('TK1001','BRS','ANK',45,450,300)  #print(u1.sure)
u2 = ucus('TK3098','İST','İZMR',55,375,260)  #print(u2.kalkis)

print(u2.anons())

print(u1.satis(15))

