import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
query= 'smart phone'
file=1

for i in range(1,100):
    try:
        driver.get(f"https://www.noon.com/uae-en/search/?limit=50&originalQuery=amart%20phone&page={i}&q={query}&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
        ele=driver.find_elements(By.CLASS_NAME,"productContainer  ")
        print(f'{len(ele)} items found')
        for element in ele:
            d=element.get_attribute('outerHTML')
            with open(f"noon_phone_data1/{query}{file}.html" ,'w' , encoding='utf-8') as f:
                f.write(d)
                file +=1
    except Exception as e:
        print(e)
