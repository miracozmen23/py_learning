from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)
time.sleep(2)

driver.maximize_window() #sayfayı tam ekran yapma
print(driver.title)
driver.save_screenshot("github-homepagess.png") #ss alma

time.sleep(2)

url_2 = "http://github.com/miracozmen23"
driver.get(url_2)

print(driver.title)

time.sleep(2)

if "miracozmen" in driver.title:
    driver.save_screenshot("miracozmen23-github.png")

time.sleep(2)
driver.back() #sayfayı geri alma
# driver.forward() sayfayı ileri alma

time.sleep(2)
driver.close()
