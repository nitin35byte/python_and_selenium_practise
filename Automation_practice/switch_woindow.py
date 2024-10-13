from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH,"//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']").click()

print(driver.current_window_handle)

handle=driver.window_handles

for han in handle:
    driver.switch_to.window(han)
    print(driver.title)
    if driver.title=="Selenium":
        driver.close()

    #print(han)
    #
