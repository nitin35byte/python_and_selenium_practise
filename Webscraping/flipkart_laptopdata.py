import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
query= 'laptop'

file=0
for i in range(1 , 20):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
    eles=driver.find_elements(By.XPATH,"//div[@class='DOjaWF gdgoEp']//div[contains(@class,'cPHDOP col-12-12')]")
    print(f"{len(eles)} items found")
    for ele in eles:
        #print(ele.text)
        d=ele.get_attribute("outerHTML")
        """
        getting data and creating file for all the data
        """
        with open(f"data1/{query}{file}.html" , 'w' , encoding='utf-8') as f:
            f.write(d)
            file +=1
        