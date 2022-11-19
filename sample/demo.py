import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Register.html")

driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("suma sree")
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("pereddy")
time.sleep(2)

driver.find_element(By.ID,'checkbox1').click()
time.sleep(2)

driver.find_element(By.ID,'checkbox1').click()
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/label').click()

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys("cherukucherla(v),midthur(m),kurnool(d).")

driver.find_element(By.XPATH,'//*[@id="eid"]/input').send_keys("pereddy.suma@gmail.com")

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[4]/div/input').send_keys("8897625721")

driver.find_element(By.ID,'msdd').click()
driver.find_element(By.XPATH,'//li//a[text()="English"]').click()
driver.find_element(By.XPATH,'//li//a[text()="Arabic"]').click()

s=Select(driver.find_element(By.ID,'Skills'))
#s.select_by_index(10)
#s.select_by_visible_text("Android")
s.select_by_value("AutoCAD")

'''list=s.options
l=len(list)
for i in range(l):
    print(s.select_by_index(i))
'''

#driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span/span[2]')
#s.select_by_visible_text("Japan")


driver.find_element(By.ID,'yearbox').click()
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[11]/div[2]/select').click()
driver.find_element(By.ID,'daybox').click()


driver.find_element(By.XPATH,'//*[@id="firstpassword"]').send_keys("suma sree")
driver.find_element(By.ID,'secondpassword').send_keys("suma sree")
time.sleep(60)