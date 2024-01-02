
import tkinter as tk
from tkinter.ttk import Combobox # eğer buraya Combobox demesek * dersek bütün hepsini getirir.

def secim():
    print(combo.get())

pencere = tk.Tk()

combo = Combobox()
combo['values'] = ("Bursa", "Adana","İstanbul","Antalya")
combo.place(x=20,y=20)

btn = tk.Button(text='Yazdır', command=secim) #combo'da yazan değeri seçip butona basınca consola yazar.
btn.place(x=70,y=50)

pencere.mainloop()

