
#Dairenin Alanı
r=float(input("Yarıçap giriniz: "))
piSayisi=3.14
alan=piSayisi*(r**2)
cevre=2*piSayisi*r

print("alan: "+str(alan) + " "+ "cevre: "+ str(cevre))

#Klavyeden girilen km bilgisini mil cinsinden hesaplayınız. 1mil = 1.609344 km

km = float(input("Kilometreyi giriniz: "))
mil = km/1.609344
mil = round(mil,2)#yuvarlama

print(str(km)+ " kilometre "+str(mil)+ " mildir")

#String parçalama(slicing)
kurs="Python ile Programlama"
adet=len(kurs)
print(kurs[0:6])
print(kurs[:6])
print(kurs[11:adet])
print(kurs[11:])
print(kurs[-11:-1])
print(kurs[0:20:2])
print(kurs[::-1])

#String Formatlama
ad="Miraç"
soyad="Özmen"
yas=21

#String f
msj = "My Name is {} {}. I'm {} years old.".format(ad,soyad,yas)
msj2 = f"My Name is {ad} {soyad}. I'm {yas} years old."
print(msj)
print(msj2)

