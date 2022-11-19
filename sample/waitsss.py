import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
#driver.implicitly_wait(40)
#driver.find_element(By.ID,'populate-text').click()
#time.sleep(15)
#print(driver.find_element(By.XPATH,'//h2[text()="Selenium Webdriver"]').is_displayed())

w=WebDriverWait(driver,10)
'''driver.find_element(By.ID,'alert').click()
EC.alert_is_present()
print(driver.current_url)'''

driver.find_element(By.ID,'enable-button').click()
EC.element_to_be_clickable(driver.find_element(By.ID,'id="disable"'))
#driver.find_element(By.ID,'id="disable"').click()