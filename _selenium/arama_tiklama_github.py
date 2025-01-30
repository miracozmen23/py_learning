from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from colorama import Fore
import time

class Github():
    def __init__(self):
        self.tarayici = Chrome()
        self.siteye_git()
        
    def siteye_git(self):
        self.tarayici.get("http://github.com")
        time.sleep(1)
        self.tarayici.maximize_window()
        time.sleep(3)
        
        self.tarayici.find_element(By.XPATH,"/html/body/div[1]/div[3]/header/div/div[2]/div/div/qbsearch-input/div[1]/button").click()
        time.sleep(3)
        arama_kutusu = self.tarayici.find_element(By.ID,"query-builder-test")
        arama_kutusu.send_keys("Python")
        time.sleep(3)
        arama_kutusu.send_keys(Keys.ENTER)
        time.sleep(10)
        
        repos = self.tarayici.find_elements(By.CLASS_NAME, "Box-sc-g0xbh4-0.flszRz")
        print(f"Bulunan repo sayısı: {len(repos)}")
        
        for i in repos:
            repo_names = i.find_element(By.CLASS_NAME,"prc-Link-Link-85e08").text
            repo_describes = i.find_element(By.CLASS_NAME,"Box-sc-g0xbh4-0.dcdlju").text
            
            print(Fore.YELLOW)
            print(repo_names)
            print(Fore.CYAN)
            print(repo_describes)
            print(Fore.RESET)
            print("*"*45)
        
        

github = Github() 