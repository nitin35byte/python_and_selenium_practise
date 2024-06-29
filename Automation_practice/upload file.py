import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.freepdfconvert.com/")

# Wait for the file upload input element to be visible and clickable
file_input = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='file']"))
)

# Provide the path of the file to be uploaded
file_path = "tet data/Test data.docx"

# Upload the file
file_input.send_keys(file_path)

# Give some time for the upload process to complete
time.sleep(5)

# Close the WebDriver
driver.quit()
