#Listele oluşturma
ogrenci=["Miraç","Özmen",75,60,90]
print(ogrenci[0] + " " + ogrenci[1])
ortalama = (ogrenci[2] + ogrenci[3] + ogrenci[4])/3
print(ortalama)

ogrenciler=[["Miraç","Özmen",75,60,90],["Alperen","Özmen",40,60,80]]
print(ogrenciler[0])
print(ogrenciler[1])
print(ogrenciler[0][2])
print(ogrenciler[1][2])

#örnek #1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ["Toyota","Bmw","Renault","Mercedes"]

#2- Liste kaç elemanlıdır?
print(len(markalar))

#3- Listenin ilk ve son elemanı nedir?
print("ilk eleman: "+markalar[0]+" son eleman: "+markalar[-1])

#4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2]="Togg"

#5- "Togg" listenin bir elemanı mıdır?
iselement="Togg" in markalar
isnotelement="Togg" not in markalar
print(iselement) 
print(isnotelement) 

#6- Listenin ilk 2 elemanını alınız.
first_two_element = markalar[0:2]
print(first_two_element)

#7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
update_list=markalar + ["Ford","Citroen"]
print(update_list)

#8- Listenin son elemanını siliniz.
del(markalar[-1])
print(markalar)

#9- Aşağıdakı verileri liste içerisinde saklayınız.
    #öğrencil: Yiğit Bilgi 2010 (70,80,90]
    #öğrenci2: Ada Bilgi 2011 [70,70,80]
    #öğrenci3: Çınar Turan 2017 (60,60,90]
ogrencilerr=[["Yiğit Bilgi", 2010, [70,80,90]],["Ada Bilgi", 2011, [70,70,80]],["Çınar Turan", 2017, [60,60,90]]]
print(ogrencilerr)

#10- Öğrencilerin yaşlarını hesaplayınız.
bu_yil=2024
yaslar=[bu_yil-ogrencilerr[0][1] , bu_yil-ogrencilerr[1][1] , bu_yil-ogrencilerr[2][1]]
print(yaslar)

#11- Öğrencilerin not ortalamalarını hesaplayınız.
ortalamalar=[[(ogrencilerr[0][2][0]+ogrencilerr[0][2][1]+ogrencilerr[0][2][2])/3],
[(ogrencilerr[1][2][0]+ogrencilerr[1][2][1]+ogrencilerr[1][2][2])/3],
[(ogrencilerr[2][2][0]+ogrencilerr[2][2][1]+ogrencilerr[2][2][2])/3]]
print(ortalamalar)
