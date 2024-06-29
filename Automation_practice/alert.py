import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome driver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://demo.automationtesting.in/Alerts.html")

# Handling Alert with OK button
driver.find_element(By.XPATH, "//a[text()='Alert with OK ']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display an')]").click()
alert = driver.switch_to.alert
alert.accept()
time.sleep(2)  # Adding a small delay to ensure the alert is closed

# Handling Alert with OK & Cancel button
driver.find_element(By.XPATH, "//a[contains(text(),'Alert with OK & Cancel ')]").click()
driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display a confirm box ')]").click()
confirm_alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
print("Alert text:", confirm_alert.text)
confirm_alert.dismiss()

driver.find_element(By.XPATH,"//a[contains(text(),'Alert with Textbox ')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'click the button to demonstrate the prompt box ')]").click()

confirm_alert_1= WebDriverWait(driver,10).until(EC.alert_is_present())
print("Alert text:", confirm_alert_1.text)
confirm_alert_1.send_keys("Nitin")
confirm_alert_1.accept()
# Close the browser
driver.quit()