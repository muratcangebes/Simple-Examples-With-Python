#if <koşul>:
#   <koşul sağlanıyorsa bu kısmı çalıştır>
#elif <alternatif koşul>:
#   <alternatif koşul sağlanıyorsa bu kısmı çalıştır
#else:
#   <koşul sağlanmıyorsa bu kısmı çalıştır>

hd="yağmurlu"
if(hd=='yağmurlu'):
    print("Şemsiye al")
elif(hd=='karlı'):
    print("Atkı al")
else:
    print("Normal")
