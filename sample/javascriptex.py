import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://www.amazon.in/")
'''driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('iphone')
btn = driver.find_element(By.ID, 'nav-search-submit-button')
driver.execute_script("arguments[0].click();",btn)'''

txtbx=driver.find_element(By.ID,'twotabsearchtextbox')
#driver.execute_script("arguments[0].setAttribute('style','background: red; border:5px solid yellow;');",txtbx)

#driver.execute_script("window.scroll(200,500)")
sig=driver.find_element(By.XPATH,'//a[text()="Australia"]')
driver.execute_script("arguments[0].scrollintoview();",sig)
#sig.location_once_scrolled_into_view

time.sleep(5)