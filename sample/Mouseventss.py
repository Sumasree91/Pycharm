import time

from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
'''driver.get("https://jqueryui.com/droppable/")
a=ActionChains(driver)
driver.switch_to.frame(0)
src=driver.find_element(By.ID,'draggable')
tgt=driver.find_element(By.ID,'droppable')
a.drag_and_drop(src,tgt).perform()'''


driver.get("https://jqueryui.com/slider/")
a=ActionChains(driver)
driver.switch_to.frame(0)
src=driver.find_element(By.ID,'slider')
a.drag_and_drop_by_offset(src,100,150).perform()
#a.scroll(100,100).perform()

time.sleep(30)




time.sleep(10)