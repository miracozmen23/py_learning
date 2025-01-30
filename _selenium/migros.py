import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from colorama import Fore

class Migros():
    def __init__(self):
        self.tarayici=Chrome()
        self.siteye_git()
        
    def siteye_git(self):
        for i in range(1,4):
            self.tarayici.get(f"https://www.migros.com.tr/et-tavuk-balik-c-3?sayfa={i}&sirala=onerilenler")
            time.sleep(3)
            kutu = self.tarayici.find_element(By.TAG_NAME,"div").find_elements(By.TAG_NAME,"sm-list-page-item")
            for i in kutu:
                content = i.find_element(By.ID,"product-name").text
                fiyat = i.find_element(By.TAG_NAME,"fe-product-price").text
                image = i.find_element(By.CLASS_NAME,"product-link").get_attribute("href")
                
                print(Fore.LIGHTRED_EX)
                print(content)
                print(Fore.BLUE)
                print(fiyat)
                print(Fore.GREEN)
                print(image)
                print(Fore.RESET)
                print("*"*45)
                
migros = Migros()