markalar = ["opel","bmw","togg"]
for index,marka in enumerate(markalar,1):
     print(f"{index}-{marka}")
     
        
numara = [100,200,300]
ogrenci = ["Ali","Ayşe","Canan","Mehmet"]

print(list(zip(numara,ogrenci)))

for no,isim in zip(numara,ogrenci):
    print(no,isim)