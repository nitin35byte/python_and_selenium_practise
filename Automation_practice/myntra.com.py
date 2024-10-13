import time

import pandas as pd
from selenium import  webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait


option= webdriver.ChromeOptions()
#option.add_argument("--headless")

driver =webdriver.Chrome(options=option)
driver.get("https://www.flipkart.com/")
page_title= driver.title
print(page_title)

assert page_title =="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
#try:
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("vivo")
search_box.send_keys(Keys.ENTER)

listed_item= driver.find_elements(By.XPATH,"//div[@class='cPHDOP col-12-12']")
# for product in listed_item:
#     product.click()

#print(product.text)
product_name=[]
count=0
produc_name = driver.find_elements(By.XPATH, "//div[@class='KzDlHZ']")
#listed_item= driver.find_elements(By.XPATH,"//div[@class='cPHDOP col-12-12']")
for product in listed_item:
    product.click()
    #product_name.append(product.text)
    add_to_cart=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"(//button[normalize-space()='Add to cart'])[1]")))
    add_to_cart.click()
    count +=1
    driver.back()
print(product_name)
#
# output_file = 'amazon_cart_items.xlsx'
#      #Create a DataFrame from the extracted items
#     df = pd.DataFrame({'Item Name': cart_items})
#
#      #Export the DataFrame to Excel
#     df.to_excel(output_file, index=False)
#
#     #print(f"Extracted items from Amazon cart saved to '{output_file}'.")