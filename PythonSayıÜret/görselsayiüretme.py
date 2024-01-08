from tkinter import *
import random
pencere=Tk()

def sayi():
    a=random.randint(0,100)
    yazi["text"]=a

pencere.title("Örnek Uygulama")
pencere.geometry("300x300+15+15")
pencere.resizable(width="FALSE", height="FALSE")

yazi=Label(text="Sayı üretmek için butona basınız...")
yazi.pack()

btn=Button(pencere, text="Sayı Üret", command=sayi)
btn.pack()

mainloop()
