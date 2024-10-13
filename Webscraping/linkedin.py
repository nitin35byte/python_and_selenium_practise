import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/home")
driver.find_element(By.XPATH,"//a[contains(@class,'nav__button-secondary')]").click()
driver.find_element(By.ID,"username").send_keys("nitti0407@gmail.com")
driver.find_element(By.ID,"password").send_keys("Nitin0407@")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
print(driver.title)

jobs=WebDriverWait(driver , 10).until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//span[text()='Jobs']")))
jobs.click()

see_more=WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.CLASS_NAME ,"artdeco-button__text")))
see_more.click()

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height




