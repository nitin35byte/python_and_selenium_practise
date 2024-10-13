import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
query= 'smart phone'
file=0
for i in range(1,25):
    try:
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=1L0Q91SOR1BM2&qid=1728112422&sprefix=smatrphone%2Caps%2C218&ref=sr_pg_2")
        ele=driver.find_elements(By.CLASS_NAME,"puis-card-container")
        print(f'{len(ele)} items found')
        for element in ele:
            d=element.get_attribute('outerHTML')
            with open(f"phone_data/{query}{file}.html" ,'w' , encoding='utf-8') as f:
                f.write(d)
                file +=1
    except Exception as e:
        print(e)

