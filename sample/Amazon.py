import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://www.amazon.in/")

driver.find_element(By.XPATH,'//*[@id="nav-xshop"]/a[2]').click()
#driver.find_element(By.XPATH,'//a[text()='Mobiles'](1)')

driver.find_element(By.XPATH,'//a[text()='Customer Service']//following::a[text()='Mobiles']')
time.sleep(10)



















time.sleep(30)