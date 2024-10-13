import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
title=driver.title
print(title)

assert title =='Practice Page'

select =Select(driver.find_element(By.ID,"dropdown-class-example"))
# select.select_by_visible_text('Option3')
# select.select_by_index(0)

select.select_by_value('option3')

driver.implicitly_wait(10)
action=ActionChains(driver)
#driver.execute_script("window.scrollTo(0 , 500)")
#element=driver.find_element(By.ID,'mousehover')
#driver.execute_script('arguments[0].scrollToView();',element)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
action.click_and_hold(driver.find_element(By.LINK_TEXT,'Top')).perform()
time.sleep(10)
print("hello")