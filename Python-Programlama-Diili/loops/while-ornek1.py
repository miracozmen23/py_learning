# 1- Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.
bas=int(input("Başlangıç değeri:"))
son=int(input("Bitiş değeri:"))

while(bas<son):
     if(bas %2 == 0):
         print(bas)
     bas += 1

# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.
a=100
while(a>0):
     print(a)
     a -= 1

# 3- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
say=1
sayilar = []

while(say<6):
     sayi = int(input(f"{say}.Sayı:"))
     sayilar.append(sayi)
     say += 1
sayilar.sort()
print(sayilar)

# 4- Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.
username = ""

while not username:
    username = input("kullanıcı adı: ")

print("girilen username: " + username)
