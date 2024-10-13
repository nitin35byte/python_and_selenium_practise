from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.99acres.com/search/property/buy/pune?city=19&keyword=pune&preference=S&area_unit=1&res_com=R")

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup=BeautifulSoup(driver.page_source , 'lxml')
properties=soup.find_all('div' , class_='PseudoTupleRevamp__outerTupleWrap')


for property in properties:
    property_name=property.find('div' , class_='PseudoTupleRevamp__contactSubheading').text
    Property_status = property.find('div', class_='ImgItem__fomoWrap').text
    property_price = property.find('div', class_='cc__CarouselBox').text
    property_description = property.find('p', class_='descPtag_undefined tupleNew__descText').text
    upper_header = property.find('div', class_='PseudoTupleRevamp__heading').text
    middle_tab_data = property.find('div', class_='cc__CarouselContainer').text
    near_by = property.find('div', class_='tupleNew__highlightsWrap').text

    print(middle_tab_data)