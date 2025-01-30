from twitter_user_info import username,password
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from colorama import Fore

class Twiitter():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = Chrome()
    
    def signIn(self):
        self.browser.get("https://x.com/i/flow/login")
        time.sleep(3)
        
        uname_box = self.browser.find_element(By.NAME,"text")
        uname_box.send_keys(self.username)
        uname_box.send_keys(Keys.ENTER)
        time.sleep(3)
        
        password_box = self.browser.find_element(By.NAME,"password")
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(3)
        
    def search(self,hashtag):
        search_box = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input")
        search_box.send_keys(hashtag)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        
        tum_twit = self.browser.find_elements(By.CLASS_NAME,"css-175oi2r.r-18u37iz.r-1udh08x.r-1c4vpko.r-1c7gwzm.r-o7ynqc.r-6416eg.r-1ny4l3l.r-1loqt21")
        for i in tum_twit:
            twits = i.find_element(By.CLASS_NAME,"css-146c3p1.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim").text
            print(twits)
            print("*"*45)
        
twitter = Twiitter(username,password)
twitter.signIn()
twitter.search("python")