
import tkinter as tk

isimler = ["Buse","Burak","MURAT","Berk","Azra","Merlin","Harry","ERDEM"]

def sil():
    liste.delete(tk.ACTIVE)
def temizle():
    liste.delete(0,tk.END)


pencere=tk.Tk()

liste = tk.Listbox()
liste.place(x=10,y=10)

for i in isimler:
    liste.insert(tk.END,i)

btnsil = tk.Button(pencere,text="SİL",command=sil)
btnsil.place(x=140,y=10)

btntemizle = tk.Button(pencere,text="TEMİZLE",command=temizle)
btntemizle.place(x=140,y=30)

pencere.mainloop()

