import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.redbus.in/")

driver.find_element(By.ID,"src").send_keys("de")
time.sleep(15)
pickup=driver.find_elements(By.XPATH,"//li[@class='sc-iwsKbI jTMXri']")
for pick in pickup:
    data=pick.text
    print(data)
    if data =="Deedwana":
        pick.click()
        time.sleep(4)

