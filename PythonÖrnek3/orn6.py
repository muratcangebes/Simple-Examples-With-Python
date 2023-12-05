a= int(input("Sayı 1= "))
b= int(input("Sayı 2= "))
c= int(input("Sayı 3= "))

if(a>b and a>c and b>c):
    print("{} > {} > {}".format(a,b,c))
elif(a>b and a>c and c>b):
    print("{} > {} > {}".format(a,c,b))
elif(b>a and b>c and a>c):
    print("{} > {} > {}".format(b,a,c))
elif(b>a and b>c and c>a):
    print("{} > {} > {}".format(b,c,a))
elif(c>a and c>b and b>a):
    print("{} > {} > {}".format(c,b,a))
elif(c>a and c>b and a>b):
    print("{} > {} > {}".format(c,a,b))
