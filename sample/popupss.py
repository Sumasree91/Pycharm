import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win332\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Alerts.html")
#driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
#driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button').click()
#driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="Textbox"]/button').click()
driver.switch_to.alert.send_keys("good morning team")
driver.switch_to.alert.accept()


#time.sleep(10)
#driver.switch_to.alert.accept()

time.sleep(5)