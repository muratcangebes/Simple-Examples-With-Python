from collections import Counter
sarki="""Nikâhına beni çağır, sevgilim
İstersen şahidin olurum senin
"Bu adam kim?" diye soran olursa
"Eski bir tanıdık" dersin, sevgilim

Nikâhına beni çağır sevgilim
İstersen şahidin olurum senin
Bu adam kim diye soran olursa
"Eski bir tanıdık" dersin, sevgilim

Hayaller kurardık biz yıllar önce
Hiç yoktu hesapta ayrılık bizce
Bilirsin ne kadar görmek isterdim
Beyazlar içinde seni öylece"""

print(Counter(sarki))
print(sarki.split())
print(Counter(sarki.split()))


