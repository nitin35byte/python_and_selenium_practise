from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import by

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Alerts.html")

WebDriverWait(driver , 20).until(EC.)