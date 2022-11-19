import time

from select import select
selenium import webdrivefromr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

list=[]
driver=webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Register.html")
'''s=Select(driver.find_element(By.ID,'Skills'))
list=s.options
l=len(list)
for i in range(l):
    print(s.select_by_index(i))
#s.select_by_index(4)
#s.select_by_visible_text("Unix")
'''
'''
list=["English","French","Arabic"]
driver.find_element(By.ID,'msdd').click()
for i in list:
    driver.find_element(By.XPATH,'//li//a[text()="'+i+'"]').click()'''


'''driver.find_element(By.ID,"msdd").click()
driver.find_element(By.XPATH,'//li//a[text()="English"]').click()
driver.find_element(By.XPATH,'//li//a[text()="Spanish"]').click()'''

d=driver.find_element(By.ID,'Skills')
List=d.find_element(By.TAG_NAME,'option')
for i in List:
    print(i.get_attribute('value'))

time.sleep(60)
