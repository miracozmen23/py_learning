from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.common.keys import Keys

class web_otomasyonu():
    def __init__(self):
        self.yazilar = []
        self.tarayici = Chrome()  
        self.siteye_git()
        self.veri_cek()
        self.kutuya_tikla()
    
    def siteye_git(self):
        self.tarayici.get("https://www.m5bilisim.com/tr/on-parmak/hiz-testi/")
        sleep(2)
        
    def veri_cek(self):
        yazilar = self.tarayici.find_element(By.ID, "satir").find_elements(By.TAG_NAME, "span")
        for i in yazilar:
            if i:
                print(i.text)
                self.yazilar.append(i.text)
    
    def kutuya_tikla(self):
        yazi_kutusu = self.tarayici.find_element(By.XPATH, '//*[@id="yaziyaz"]')
        for i in self.yazilar:
            yazi_kutusu.send_keys(i)
            sleep(1)
            yazi_kutusu.send_keys(Keys.SPACE)
            sleep(1)

web_otomasyonu()
