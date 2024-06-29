import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
driver.find_element(By.XPATH,"//table[contains(@id,'customers')]")
time.sleep(10)
tables=driver.find_elements(By.XPATH,"//table[contains(@id,'customers')]//tr")
for table in tables:
    print(f"table contents are :",table.text)

tb=driver.find_elements(By.XPATH,"//table[contains(@id,'customers')]//tr//th")

for table in tb:
    print(f"table contents are :",table.text)