sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ['ahmet','canan','zeynep','gökhan','ali','canan']

print(min(sayilar))
print(min(isimler))
print(max(isimler))
print(max(sayilar))

# ekleme
sayilar.append(12)
isimler.append('çınar')

sayilar.insert(0, 100)
sayilar.insert(-1, 100)
sayilar.insert(-3, 100)
sayilar.insert(len(sayilar), 100)

print(sayilar)
print(isimler)

# silme
sayilar.pop()
sayilar.pop(0)
isimler.remove('canan')

print(sayilar)
print(isimler)


#sıralama
sayilar.sort()
isimler.sort()
sayilar.reverse()
isimler.reverse()

print(sayilar)
print(isimler)

# arama
#çalıştırırken ekleme ve silme kısmındaki kodları yorum satırına almayı unutma
sonuc = sayilar.index(4)

sonuc = sayilar.count(4)
sonuc = isimler.count('canan')

print(sonuc)