yemekTarifi = {
    "yemekAdi":"Musakka",
    "yemekTarifi":"tarif açıklaması",
    "resim":"1.jpg"
}

#access items
print(yemekTarifi.get("yemekAdi"))
print(yemekTarifi.keys())
print(yemekTarifi.values())
print(yemekTarifi.items())

#update items
yemekTarifi.update({"yemekAdi" : "Manti"})
sonuc = yemekTarifi
print(sonuc)

#delete items
yemekTarifi.pop("yemekAdi")
sonuc2=yemekTarifi
print(sonuc2)
