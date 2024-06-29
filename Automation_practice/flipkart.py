from selenium import webdriver
import time
import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(5)
titlet=driver.title
print("title of the page is :",titlet)


action=ActionChains(driver)
element = driver.find_element(By.XPATH,"//*[@aria-label='Myntra']")
action.scroll_to_element(element).perform()
driver.execute_script("window.scrollTo(0, 0);")

element.click()
driver.switch_to.window(driver.window_handles[1])
print(driver.current_url)
main_window_handle = driver.current_window_handle
all_links=driver.find_elements(By.TAG_NAME,"a")
for links in all_links:
    print(links.get_attribute("href"))

original_window_handle=driver.window_handles[0]
driver.switch_to.window(original_window_handle)
print(driver.current_url)
# Get all window handles


all_window_handles = driver.window_handles
# Switch to the new window/tab
for window_handle in all_window_handles:
    if window_handle != main_window_handle:
        driver.switch_to.window(window_handle)
        break

# Now you're in the new window/tab, perform actions as needed
new_window_title = driver.title
print("Title of the new window:", new_window_title)

driver.switch_to.window(main_window_handle)

main_window_title = driver.title
print("Title of the main window:", main_window_title)

# driver.find_element(By.XPATH,"//span[text()='Login']").click()
# driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").clear()
# driver.find_element(By.XPATH,"//input[@class='r4vIwl BV+Dqf']").send_keys("0987890444")
# driver.find_element(By.XPATH,"//button[text()='Request OTP']").click()
# error_mmessge=driver.find_element(By.XPATH,"//span[@class='llBOFA']")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# error_mmessge=error_mmessge.text
# print(error_mmessge)
# assert   error_mmessge=="Please enter valid Email ID/Mobile number"
#
#
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# expected=driver.find_element(By.XPATH,"//*[@class='EpHS0A']").text
# print(expected)
# actual_text="By continuing, you agree to Flipkart's"
# if expected==actual_text:
#     assert True
