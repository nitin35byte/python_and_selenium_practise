import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.support.ui import WebDriverWait
def generic_date_selection(target_month , target_year , target_date):
    while True:
        date_picker_header=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='DayPicker-Caption'])[1]")))
        year_month=date_picker_header.text

        current_month=year_month.split()[0]
        current_year=year_month.split()[1]
        print(current_month)
        print(current_year)
        if current_month == target_month and current_year==target_year:
            driver.find_element(By.XPATH,f"(//p[text()='{target_date}'])[1]").click()
            break
        else:
            next_btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[@aria-label='Next Month']")))
            next_btn.click()
            time.sleep(1)


target_month, target_year, target_date='June' , 2025 , 1
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
close=WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME,"commonModal__close")))
close.click()
WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//label[@for='departure']"))).click()
generic_date_selection(target_month, target_year, target_date)
print("pass")