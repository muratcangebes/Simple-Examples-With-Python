
import tkinter as tk

def sayi_tikla (sayi):
    a = 0
    if  a==1:
        giris.delete(0,tk.END)
    mevcut = giris.get()
    giris.delete(0,tk.END)
    giris.insert(tk.END, mevcut+str(sayi))
    if sayi == '=':
        a += 1

def temizle():
    giris.delete(0,tk.END)


def hesapla():
    try:
        sonuc = eval(giris.get())
        giris.delete(0,tk.END)
        giris.insert(tk.END,str(sonuc))
    except Exception as hata:
        giris.delete(0,tk.END)
        giris.insert(tk.END,"HATA")


pencere= tk.Tk()
pencere.title("Hesap Makinesi")

giris=tk.Entry(pencere, width=20)
giris.grid(row=0,column=0,columnspan=4)

butonlar = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+',]

row_val = 1
col_val = 0

for button in butonlar:
    if button == '=':
        tk.Button(pencere,text=button,width=4,height=2,command=hesapla).grid(row=row_val,column=col_val)
    else:
        tk.Button(pencere, text=button, width=4, height=2,
                  command=lambda b=button: sayi_tikla(b)).grid(row=row_val, column=col_val)


    col_val+=1
    if col_val>3:
        col_val=0
        row_val+=1

tk.Button(pencere,text='C',width=20,height=2,command=temizle).grid(row=row_val,column=col_val,columnspan=4)


pencere.mainloop()

