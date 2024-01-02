
import tkinter as tk
from tkinter import *

def csec():
    print("Seçim-1 : ", c1.get())
    print("Seçim-2 : ", c2.get())

def rsec():
    print("Aktif Seçim : ", r.get())


penc = tk.Tk()

c1 = IntVar()
c2 = IntVar()
cb1 = Checkbutton(text="SEÇİM-1", variable=c1,
                  onvalue=1,offvalue=0, command=csec)

cb2 = Checkbutton(text="SEÇİM-2", variable=c2,
                  onvalue=1,offvalue=0, command=csec)

cb1.place(x=20,y=20)
cb2.place(x=20,y=60)


r = IntVar()
rb1 = Radiobutton(text="Bağlı Seçim - 1", variable=r,
                  value=1, command=rsec)

rb2 = Radiobutton(text="Bağlı Seçim - 2", variable=r,
                  value=2, command=rsec)

rb1.place(x=100,y=20)
rb2.place(x=100,y=50)
penc.mainloop()

