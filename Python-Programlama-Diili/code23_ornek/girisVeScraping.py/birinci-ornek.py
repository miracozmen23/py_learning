import requests
from bs4 import BeautifulSoup

data = requests.get("https://tr.wikipedia.org/wiki/Finans").content

print(data)

data = BeautifulSoup(data,"html.parser")

print(data.prettify())

baslik = data.find("span","mw-page-title-main").text
print(baslik)

aciklama = data.find_all("p")[0:2]
for i in aciklama:
    try:
        print("https://tr.wikipedia.org"+i.find("a",["href"]))
        print(i.text)
    except:
        continue
