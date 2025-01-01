from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(15)
title=driver.title
print(title)

main_window= driver.current_window_handle
print(main_window)
assert title=="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
text='Happy New Year'
print(f"All Good :",text)
elemnt_to_scroll=driver.find_element(By.XPATH ,"//a[normalize-space()='Myntra']")
driver.execute_script("window.scrollTo(0 ,document.body.scrollHeight);")
#driver.execute_script("arguments[0].scrollIntoView(true);",elemnt_to_scroll)
elemnt_to_scroll.click()

all_window= driver.window_handles

for handle in all_window:
    print(handle)
    if handle!=main_window:
        driver.switch_to.window(handle)
        break

print("New window title:", driver.title)

driver.close()

# Switch back to the main window
driver.switch_to.window(main_window)

# Perform actions in the main window
print("Main window title:", driver.title)

# Quit the driver
driver.quit()


# Scroll down by 500 pixels
driver.execute_script("window.scrollBy(0, 500);")