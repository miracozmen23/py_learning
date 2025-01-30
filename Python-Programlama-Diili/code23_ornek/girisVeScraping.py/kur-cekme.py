import requests
from bs4 import BeautifulSoup
from time import sleep
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import numpy as np
import datetime

# data = yf.download("GARAN.IS",start="2018-01-01")
# plt.title("Garan Kapanış")
# data["Hareketli_Ortalama"]= data["Close"].rolling(window = 112).mean()
# plt.plot(data["Close"],label="kapanış değeri",color ="green")
# plt.plot(data["Hareketli_Ortalama"],label="hareketli ortalama",color ="red")

# plt.legend()
# plt.grid()
# plt.show()


class DolarKuru():
    def __init__(self) :
        self.data =[]
        self.veri_cek()
        
    def veri_cek(self):
        for i in range(1,45):
            data = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari").content
            data = BeautifulSoup(data,"html.parser")
            buyuk_kutu = data.find("div",{"class":"flex justify-between mt-8"})
            dolar_bul = buyuk_kutu.find("div",{"data-socket-key":"USD"}).text
            self.data.append(dolar_bul)
            tarih = datetime.datetime.now()
            print(f"Tarih: {tarih} Dolar kuru:",dolar_bul)
            sleep(1)
    
    def grafik_cizim(self):
        dizi= np.array(self.data)
        plt.title("anlık dolar kuru")
        plt.plot(dizi)
        plt.plot(dizi,label="kapanış değeri")
        plt.legend()
        plt.grid()
        plt.show
        
                
t=DolarKuru()