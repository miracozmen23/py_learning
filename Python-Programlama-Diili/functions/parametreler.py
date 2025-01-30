import datetime
def yil():
    return datetime.datetime.now().year

def saat():
    return datetime.datetime.now().hour

def yasHesapla():
    return yil()-2003

def selamlama():
    if(saat()<12):
        return "Günaydın"
    else:
        return "Merhaba"

print(yasHesapla())
print(selamlama())
print(saat())