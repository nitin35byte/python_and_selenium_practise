from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
location='pune'
file=0
driver = webdriver.Chrome()
for i in range(0,50):
     try:
          driver.get(f"https://www.99acres.com/search/property/buy/{location}?city=19&preference=S&area_unit=1&res_com=R")
          products=driver.find_elements(By.CLASS_NAME,"PseudoTupleRevamp__tupleWrap undefined")
          print(f'{len(products)} items found')
          for prod in products:
               p = prod.get_attribute("outerHTML")
               with open(f"properties/{location}{file}.html", 'w', encoding='utf-8') as f:
                    f.write(p)
                    file += 1
                    time.sleep(2)
     except Exception as e:
          print(e)

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height


# # link =driver.find_elements(By.CLASS_NAME , 'PseudoTupleRevamp__contactHeading')
# # for links in link:
# #     print(links.text)
# #     print(links)
#
# Property_provided_by= driver.find_elements(By.CLASS_NAME , 'PseudoTupleRevamp__contactSubheading')
# bhk=driver.find_elements(By.CLASS_NAME ,'PseudoTupleRevamp__FW6')
# location=driver.find_elements(By.CLASS_NAME ,'PseudoTupleRevamp__w400Ml4')
# price=driver.find_elements(By.CLASS_NAME ,'configs__ccl2')
# proprty_age=driver.find_elements(By.XPATH ,'//span[contains(@class,"ImgItem__m12 ImgItem__colorN200")]')
# competion_date=driver.find_elements(By.XPATH ,'//div[contains(@class,"tupleNew__imgCount")]')
# booking=driver.find_elements(By.CLASS_NAME ,'tupleNew__priceAndPerSqftWrap')
# for links in booking:
#      print(links.text)
#
#

# soup = BeautifulSoup(driver.page_source, 'lxml')
# listed_property = soup.find_all('div', class_='PseudoTupleRevamp__outerTupleWrap')
#  #print(listed_property)

#
# for propert in listed_property:
#      location = propert.find('a' , class_='PseudoTupleRevamp__contactSubheading').text
#      print(location)