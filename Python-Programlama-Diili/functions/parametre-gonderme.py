def yasHesapla(dogumYili):
    return 2024-dogumYili

def emekliligeKacYilKaldi(dogumYili,isim):
    yas =yasHesapla(dogumYili)
    
    kalanSure = 65-yas
    
    if(kalanSure>0):
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı."
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz."

print(emekliligeKacYilKaldi(2003,"Miraç"))
print(emekliligeKacYilKaldi(1957,"Ahmet"))
        