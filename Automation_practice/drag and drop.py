
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Accepted%20Elements")
driver.find_element(By.ID,"Accepted Elements").click()
time.sleep(5)
frame = WebDriverWait(driver,  20).until(
    EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame lazyloaded']"))
)

element_to_drop=driver.find_element(By.ID,"draggable-nonvalid")
ared_to_drop=driver.find_element(By.ID,"droppable")

action = ActionChains(driver)
action.drag_and_drop(element_to_drop,ared_to_drop).perform()
