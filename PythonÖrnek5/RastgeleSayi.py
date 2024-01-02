
import tkinter as tk
from tkinter import StringVar, IntVar
import random

# Kullanıcıdan alınan sayıları saklayacak liste
user_numbers = []

# Rastgele çekilen sayıları saklayacak liste
random_numbers = []

# Kullanıcıdan alınan başlangıç ve bitiş değerleri
start = IntVar()
end = IntVar()

# Kullanıcıdan alınan sayıları listeye ekleyen fonksiyon
def add_number():
    num = int(number_entry.get())
    user_numbers.append(num)
    user_list.insert(tk.END, num)

# Rastgele sayıları çeken ve listeye ekleyen fonksiyon
def generate_numbers():
    for _ in range(5):
        num = random.randint(start.get(), end.get())
        random_numbers.append(num)
        random_list.insert(tk.END, num)

# Doğru ve yanlış tahmin sayısını bulan fonksiyon
def compare_lists():
    correct = len(set(user_numbers) & set(random_numbers))
    incorrect = 5 - correct
    result_string.set(f"Doğru tahmin: {correct}, Yanlış tahmin: {incorrect}")

# Arayüz oluşturma
root = tk.Tk()

start_entry = tk.Entry(root, textvariable=start)
start_entry.pack()

end_entry = tk.Entry(root, textvariable=end)
end_entry.pack()

number_entry = tk.Entry(root)
number_entry.pack()

add_button = tk.Button(root, text="Sayı Ekle", command=add_number)
add_button.pack()

generate_button = tk.Button(root, text="Sayıları Üret", command=generate_numbers)
generate_button.pack()

compare_button = tk.Button(root, text="Listeleri Karşılaştır", command=compare_lists)
compare_button.pack()

user_list = tk.Listbox(root)
user_list.pack()

random_list = tk.Listbox(root)
random_list.pack()

result_string = StringVar()
result_label = tk.Label(root, textvariable=result_string)
result_label.pack()

root.mainloop()
