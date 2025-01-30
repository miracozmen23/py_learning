for i in range(1,100,2):
     print(i)

#liste oluşturma
rng = range(10)
rng = range(10,20)
rng = range(100,200,10)
rng = range(0,-20,-1)

sonuc = list(rng)
print(sonuc)

for i in range(50,250):
    if(i%2==0):
        print(i)
        
#100 e kadar olan asal sayıları yazdırma örneği

for x in range(2,100):
    for y in range(2,x):
        if(x % y == 0):
            break
    else :
        print(x)