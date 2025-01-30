#tüm harfleri büyütür
s1 = "Python Dersleri"
sonuc = s1.upper()
print(sonuc)

#tüm harfleri küçültür
s2="MERHABA"
sonuc2=s2.lower()
print(sonuc2)

#verilen stringi başlık yapar
s3="güzel bir gün"
sonuc3=s3.title()
print(sonuc3)

#verilen stringin sadece baş harfini büyük yapar
s4="güzel bir gün"
sonuc4=s4.capitalize()
print(sonuc4)

#büyük harfle mi küçük harfle mi başlıyor kontrolü
s5="güzel bir gün"
sonuc5=s5.islower() #büyük harf için s5.isupper() kullanılır
print(sonuc5)

#stringin başındaki ve sonundaki boşlukları siler
s6="  güzel bir gün"
print(s6)
sonuc6=s6.strip()
print(sonuc6)

#stringin içindeki boşluklara kadar olan kelimeleri liste şeklinde döndürür
s7="güzel bir gün"
sonuc7=s7.split()
print(sonuc7)
#bu şekilde ayırmak istediğimiz karakteri yazabiliriz 
#indexe ulaşmak istersek splitin yanına [0] vb ekleyerek istediğimiz indexe ulaşabiliriz
s7="güzel, bir gün ,evet"
sonuc7=s7.split(',') 
print(sonuc7)

#string içindeki kelimeyi değiştirme
s8 = "Bugün güneşli"
print(s8)
sonuc8 = s8.replace("güneşli","yağmurlu")
print(sonuc8)

#aranan string veya charın indexini bulur

s9 = "Bugün güneşli"
sonuc9 = s9.find('güneşli')
sonuc10= s9.index('e') 
sonuc11= s9.find('bulutlu') #find()ile bulunamayan bir karakter veya string olursa -1 gönderir
#sonuc12= s9.index('q')     #index()ile bulunamayan bir karakter veya string olursa exceptin(hata) gönderir

print(sonuc9)
print(sonuc10)
print(sonuc11)
#print(sonuc12)