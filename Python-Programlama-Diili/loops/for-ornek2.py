urunler = [
    {"urunAdi":"Hp Victus 1", "fiyat": 32999},
    {"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
    {"urunAdi":"Apple Macbook", "fiyat": 49999},
    {"urunAdi":"Huawei Matebook", "fiyat": 26999},
    {"urunAdi":"Casper Nirvana", "fiyat": 20000},
    {"urunAdi":"Hp Victus 2", "fiyat": 30000},
]

# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#    "Hp Victus marka ürünün fiyatı 32999 Türk Lirası."
for i in urunler:
    print(f"{i['urunAdi']} marka ürünün fiyatı {i['fiyat']} TL.")

# 2- Ürünlerin fiyatları toplamı nedir?
top=0
for j in urunler:
    top += j['fiyat']
print(f"Ürünlerin fiyatları toplamı: {top} TL.")

# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.
print("25 bin ve 40 bin arası fiyata sahip ürünler:")
for k in urunler:
    if(k['fiyat']>=25000 and k["fiyat"]<=40000):
        print(f"{k['urunAdi']} marka ürünün fiyatı {k['fiyat']} TL.")

# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.
kelime = input("aramak istediğiniz ürün: ")

for urun in urunler:
    if(urun["urunAdi"].lower().find(kelime.lower()) > -1):
        print(f"{urun['urunAdi']}")
else:       
    print("Ürün bulunamadı.")