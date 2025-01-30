# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
    {
        "ad":"Miraç Özmen",
        "hesapNo":"2323",
        "bakiye":5000,
        "ekHesap":3000,
        "userName":"miracozmen23",
        "password":"12345"
    },
    
    {
        "ad":"Mehmet Özmen",
        "hesapNo":"2610",
        "bakiye":7000,
        "ekHesap":5000,
        "userName":"mehmet123",
        "password":"54321"
    }
       
]

def menu(hesap):
    print("\n")
    print(f"Merhaba {hesap['ad']}")
    
    print("1-Bakiye Sorgulama")
    print("2-Para Çekme")
    print("3-Para Yatırma")
    
    islem = input("yapmak istediğiniz işlem: ")
    
    if(islem == "1"):
        bakiyeSorgula(hesap)
        
    elif(islem == "2") :
        paraCekme(hesap)
        
    elif(islem == "3"):
        paraYatirma(hesap)
        
    else:
        print("Yanlış Seçim Yaptınız.")
        
    menu(hesap)

def bakiyeSorgula(hesap):
    print(f"Bakiye: {hesap['bakiye']}")
    print(f"ekHesap: {hesap['ekHesap']}")
    
def paraYatirma(hesap):
    yatir = int(input("Yatırmak istediğniz miktar: "))
    hesap['bakiye'] += yatir
    print(f"Hesabınıza {yatir} TL yatırıldı.Güncel Bakiyeniz {hesap['bakiye']}")
    
def paraCekme(hesap):
    cek = int(input("Çekmek istediğiniz Miktar: "))
    if(cek > hesap['bakiye']):
        print(f"Normal hesap için Yetersiz bakiye, bakiyeniz {hesap['bakiye']} TL. ek hesaptaki bakiyeniz {hesap['ekHesap']} TL. Geri kalan Ek hesaptan çekilsin mi ?")
        cevap = input("e(evet)/h(hayır) harflerinden biriniz giriniz:")
        if(cevap.lower() == 'e'):
            ekCek = cek - hesap['bakiye']
            hesap['bakiye'] = 0
            if(ekCek>hesap['ekHesap']):
                print("Yetersiz Bakiye.")
            else:
                hesap['ekHesap'] -= ekCek
                print(f"Normal bakiyeniz bitti. Ek hesabınızdan {ekCek} TL, çekildi. Kalan ek hesap bakiyeniz {hesap['ekHesap']} TL.")       
        elif(cevap.lower() == 'h'): 
            print("Ek Hesaptan çekim yapmıyorsunuz.")
        else:
            print("Yanlış harf seçtiniz Lütfen e veya h 'den birini seçiniz.")
    else:
        hesap['bakiye'] -= cek
        print(f"{cek}TL, hesabınızdan çekildi.Kalan bakiyeniz {hesap['bakiye']} TL.")

def login():
    userName = input("userName :")
    password = input("password :")
    
    isLoggedIn = False
    
    for hesap in hesaplar:
        if(userName == hesap['userName'] and password == hesap['password']):
            isLoggedIn = True
            menu(hesap)
            break
        
    if not(isLoggedIn):
        print("kullanıcı adı veya parola hatalı.")
login()