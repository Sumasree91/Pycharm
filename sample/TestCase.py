import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win332\chromedriver.exe')
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()
driver.implicitly_wait(10)
#driver.find_element(By.XPATH,'//*[@id="carouselExampleIndicators"]/a[1]').click()
driver.find_element(By.ID,'login2').click()
driver.find_element(By.ID,'loginusername').send_keys("demo")
driver.find_element(By.ID,'loginpassword').send_keys("demo")
driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
time.sleep(10)

'''if 'demo'in driver.find_element(By.ID,'nameofuser').text:
    print("logged in successfully")'''

if 'wrong password'in driver.switch_to.alert.text:
    print("wrong password")
elif 'demo' in driver.find_element(By.ID,'nameofuser').text:
    print("logged in successfully")