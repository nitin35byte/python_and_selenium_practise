import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")

title=driver.title
print(title)

find_location=driver.find_element(By.ID,"file-upload")
file_path=r"C:\Users\Admin\Desktop\Automation\robotframework\pythonProject1\Automation_practice\file.png"
find_location.send_keys(file_path)
time.sleep(10)
driver.find_element(By.ID,"file-submit")
print("Kaam Ho gya bhai")