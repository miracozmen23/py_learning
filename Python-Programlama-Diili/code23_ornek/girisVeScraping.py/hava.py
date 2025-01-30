import requests
from bs4 import BeautifulSoup

def hava_durumu(şehir):
    data = requests.get(f"https://havadurumu15gunluk.org/havadurumu/{şehir}-hava-durumu-15-gunluk.html").content #sitenin linki burda conten kısmını aldık
    data = BeautifulSoup(data,"html.parser") #html olarka pars ettti
    data = data.find("div",{"class":"box__content"})
    hava_durumu = data.find("span",{"class":"status"}).text
    derece = data.find("span",{"class":"temp high bold"}).text
    print("hava durumu : ",hava_durumu)
    print("derece : ",derece)

hava_durumu("ankara")
    