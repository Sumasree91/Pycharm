import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(r'C:\Users\My Pc\Downloads\chromedriver_win32\chromedriver.exe')
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.implicitly_wait(10)
driver.find_element(By.ID, 'datepicker2').click()


# driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/table/tbody/tr[2]/td[4]/a').click()
def cal(yy, mm, dd):
    s = Select(driver.find_element(By.XPATH, '//select[@title="Change the month"]'))
    s.select_by_visible_text(mm)
    y = Select(driver.find_element(By.XPATH, '//select[@title="Change the year"]'))
    y.select_by_visible_text(yy)
    driver.find_element(By.XPATH, '//td//a[text()="' + dd + '"]').click()
cal("2019", "May", '8')
time.sleep(5)
