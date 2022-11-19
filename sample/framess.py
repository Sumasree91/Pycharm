import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Frames.html")
#driver.switch_to.frame(0)
#driver.switch_to.frame('SingleFrame')
driver.switch_to.frame(driver.find_element(By.ID,'singleframe'))
driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("tom")
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,'//*[@id="header"]/div[1]/div/div/div[2]/h1').text)

time.sleep(60)
