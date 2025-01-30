#    Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
#    ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
#    ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.

n = int(input("Öğrenci sayısı: "))
i=1
ogrenciler = []
while(i<=n):
    no = int(input("ogrenciNo:")),
    ad = input("ogrenciAdi:"),
    soyad = input("ogrenciSoyad:")
    
    ogrenciler.append({
        "ogrenciNo" : no,
        "ogrenciAdi": ad,
        "ogrenciSoyad":soyad
    })
    i+=1
for ogrenci in ogrenciler:
    print(f"{ogrenci['ogrenciNo']} numaralı öğrencinin adı {ogrenci['ogrenciAdi']} {ogrenci['ogrenciSoyad']}")