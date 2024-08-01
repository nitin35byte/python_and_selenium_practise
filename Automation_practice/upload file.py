import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(5)
element=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "picture")))
driver.execute_script("arguments[0].scrollIntoView();",element)
driver.find_element(By.ID, "picture").send_keys(r"C:\Users\Admin\Desktop\Automation\robotframework\pythonProject1\Automation_practice\file.png")
print("picture has been uploaded")
