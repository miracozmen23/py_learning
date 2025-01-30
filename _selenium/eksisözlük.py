import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from colorama import Fore

class eksi_sozluk():
    def __init__(self):
        self.tarayici = Chrome()
        self.siteye_git()
        
    def siteye_git(self):
        for i in range(1,100):
            self.tarayici.get(f"https://eksisozluk.com/milli-piyango-2017-yilbasi-ikramiyesi--5223811?p={i}")
            time.sleep(3)
            kutu = self.tarayici.find_element(By.ID,"entry-item-list").find_elements(By.ID,"entry-item")
            for i in kutu :
                content = i.find_element(By.CLASS_NAME,"content").text
                kullanici_adi= i.find_element(By.ID,"entry-author").text
                print(content)
                print(Fore.GREEN)
                print(kullanici_adi)
                print(Fore.RESET)
                print("*"*45)
                
                

data = eksi_sozluk()