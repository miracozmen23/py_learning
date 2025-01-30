from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from github_user_info import username,password
import time
from colorama import Fore

class Github():
    def __init__(self,username,password):
        self.browser = Chrome()
        self.username = username
        self.password = password
        self.signIn()
        
         
        
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        
        self.browser.find_element(By.ID,"login_field").send_keys(self.username)
        self.browser.find_element(By.ID,"password").send_keys(self.password)
        time.sleep(1)
        
        self.browser.find_element(By.NAME,"commit").click()
        time.sleep(3)
        
        self.browser.find_element(By.CLASS_NAME,"Button--invisible.Button--medium.Button.Button--invisible-noVisuals.color-bg-transparent.p-0").click()
        time.sleep(3)
        
        self.browser.find_element(By.CLASS_NAME,"Item__LiBox-sc-yeql7o-0.fGgDtq").click()
        time.sleep(3)
        
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[5]/main/div/div/div[1]/div/div/div[3]/div[2]/div[3]/div/a[2]").click()
        time.sleep(3)
        
        followings = self.browser.find_elements(By.CLASS_NAME,"d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted")
        time.sleep(3)
        
        print(Fore.GREEN)
        print("TAKİP ETTİKLERİM")
        print(Fore.RESET)
        print("-"*45)
        for i in followings:
            userinfo = i.find_element(By.CLASS_NAME,"d-inline-block.no-underline.mb-1").text
            print(Fore.YELLOW)
            print(userinfo)
            print((Fore.RED))
            print("*"*45)
            print(Fore.RESET)
               
github = Github(username,password)