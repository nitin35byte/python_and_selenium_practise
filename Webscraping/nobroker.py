import time

from selenium import webdriver
from bs4 import BeautifulSoup


driver= webdriver.Chrome()
driver.get("https://www.nobroker.in/property/sale/pune/multiple?searchParam=W3sibGF0IjoxOC40OTg5Njc2LCJsb24iOjczLjg5NTcyMDUsInBsYWNlSWQiOiJDaElKMTltZFd5M0F3anNSekY4UmlJYml2UTAiLCJwbGFjZU5hbWUiOiJQdW5lIENhbnRvbm1lbnQifSx7ImxhdCI6MTguNTU3NzQ0NiwibG9uIjo3My45MTI0Njc0LCJwbGFjZUlkIjoiQ2hJSmlTRnllc1hBd2pzUnJjeUZGc1B5c05FIiwicGxhY2VOYW1lIjoiUHVuZSJ9LHsibGF0IjoxOC41MjU1MjUsImxvbiI6NzMuODY3NDU1OTk5OTk5OTksInBsYWNlSWQiOiJDaElKb2NuX2NGN0F3anNSajBtdGZ2emlMTU0iLCJwbGFjZU5hbWUiOiJQdW5lIFJhaWx3YXkgU3RhdGlvbiJ9XQ==&radius=2.0&city=pune&locality=Pune%20Cantonment,Pune,Pune%20Railway%20Station")



last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup =BeautifulSoup(driver.page_source , "lxml")

listed_house=soup.find_all('div', class_="bg-white rounded-4 bg-clip-padding overflow-hidden mx-0.5p tp:border-b-0 shadow-defaultCardShadow tp:shadow-cardShadow tp:mt-0.5p  my-1.2p   tp:mx-0 tp:mb:1p						hover:cursor-pointer nb__2_XSE")
for house in listed_house:
    price=house.find('div' , class_='font-semi-bold heading-6').text
    print(price)