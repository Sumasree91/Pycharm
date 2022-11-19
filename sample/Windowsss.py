import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win332\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Windows.html")
p=driver.current_window_handle
print(p)
'''driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="Seperate"]/button').click()'''
driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="Multiple"]/button').click()
#driver.switch_to.window()
time.sleep(30)
ch=driver.window_handles
print(len(ch))
for i in ch:
    driver.switch_to.window(i)
    print(driver.current_url)

driver.switch_to.window(p)
print(driver.current_url)
