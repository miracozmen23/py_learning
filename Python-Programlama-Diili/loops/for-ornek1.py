sayilar = [3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdırınız.
for i in sayilar:
    print(i)

# 2- "sayilar" listesinde hangi sayılar 3' ün katıdır?
for x in sayilar:
    if(x%3==0):
        print(f"{x} sayısı 3'ün tam katıdır.")

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?
top=0
for a in sayilar:
    top+=a
print(f"sayılar listesinin elemanlar toplamı :{top}")

urunler = ["iphone 13","samsung s24","samsung s22","iphone 15","iphone 14"]

# 4- "urunler" listesindeki tüm iphone marka ürünleri listeleyiniz.
for j in urunler:
    indexler = j.find('iphone')    #indexlerini bulur
    if(indexler != -1):
        print(j)

# 5- "urunler" listesinde kaç adet samsung ürünü vardır?
say=0
for k in urunler:
    indexs = k.find('samsung')
    if(indexs != -1):
        say=say+1 
print(f"Listedeke {say} tane samsung ürün vardır.")