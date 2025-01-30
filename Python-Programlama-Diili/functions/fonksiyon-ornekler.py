# # 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
s = input("Bir kelime yazın: ")
sayi = int(input("kaç kere yazılacak: "))
def yaz(s,sayi):
     return print(s * sayi)
yaz(s,sayi)

# # 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def hesapla(kısa,uzun):
     alan = kısa * uzun
     cevre = 2 * (kısa + uzun)
     return print(f"dikdörtgenin çevresi {cevre}, alanı {alan} .")
hesapla(int(input("kısa kenar: ")),int(input("uzun kenar: ")))

# # 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yaziTura():
     import random
     deger = random.random()

     if(deger>0.5):
         return "Tura"
     else:
         return "Yazı"
print(yaziTura())

# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asal(sayi1,sayi2):
    if(sayi1 > sayi2):
        for i in range(sayi2,(sayi1+1)):
            for j in range(2,i):
                if(i % j == 0):
                    break
            else:
                 print(i)
    else:
            for a in range(sayi1,(sayi2+1)):
                for b in range(2,a):
                    if(a % b == 0):
                        break
                else:
                    print(a)
asal(int(input("1.sayi: ")),int(input("2.sayi: ")))

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def bolen(sayi):
    bolenler = []
    for i in range(1,(sayi+1)):
        if(sayi % i ==0):
            bolenler.append(i)
    return print(bolenler)
bolen(int(input("Sayı: ")))