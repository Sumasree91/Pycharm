import time

from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Register.html")
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("ram")
a=ActionChains(driver)
a.send_keys(Keys.TAB,"sam",Keys.TAB,"hyd",Keys.TAB,"sam@gmail.com",Keys.TAB,"123566778876").perform()
a.send_keys(Keys.TAB,Keys.SPACE).perform()
a.context_click().perform()
a.move_to_element(driver.find_element(By.XPATH,'//*[@id="header"]/nav/div/div[2]/ul/li[5]/a')).perform()





time.sleep(5)
