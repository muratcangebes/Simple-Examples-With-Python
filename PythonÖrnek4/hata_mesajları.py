# 08.12.2023 --- Hata Mesajları,Türleri


# print(5+'c') ----> TypeError

#liste = []
#print(liste[2]) ----> IndexError: list index out of range

'''

bilgi ={
    'İsim' : 'Ahmet',
    'TC' : 12345678901}

print(bilgi['Soyad']) ----> KeyError

'''



try:
    print(5+'c')
except TypeError:
    print("// Tür Uyuşmazlığı var.")
except:
    print("// HATA")
