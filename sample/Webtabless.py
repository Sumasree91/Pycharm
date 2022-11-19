import time

from selenium import webdriver
from selenium.webdriver.common.by import By
 #from selenium.webdriver.support.select import select

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://money.rediff.com/gainers")
'''ele=driver.find_element(By.XPATH,'//*[@id="leftcontainer"]/table')
c=driver.find_elements(By.TAG_NAME,'th')
c1=driver.find_elements(By.TAG_NAME,'td')
print(len(c))
for i in c1:
    print(i.text)
    '''
def cmp(cmp):
    print(driver.find_element(By.XPATH,'//td//a[contains(text(),"'+cmp+'")]//following::td[3]').text)
    #print(driver.find_element(By.XPATH,'//td//a[contaTirupatiins(text(),"' + cmp + '")]//following::td[3]').text)
cmp('Simplex Castings')







time.sleep(10)