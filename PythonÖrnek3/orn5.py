a= int(input("Sayı 1= "))
b= int(input("Sayı 2= "))
c= int(input("Sayı 3= "))

if(a>b and a>c):
    print("En büyük sayı {}".format(a))
elif(b>a and b>c):
    print("En büyük sayı {}".format(b))
elif(c>a and c>b):
    print("En büyük sayı {}".format(c))


