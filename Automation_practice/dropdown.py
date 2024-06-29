from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
select=Select(driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//p//select"))
driver.get_screenshot_as_file("file.png")
##select.select_by_index(2)
##select.select_by_value("Argentina")
select.select_by_visible_text("Argentina")
cook=driver.get_cookie()
for cookies in cook:
    print(cookies)