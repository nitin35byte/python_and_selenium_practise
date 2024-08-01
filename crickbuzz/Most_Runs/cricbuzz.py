import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
recent_tours=[]
upcoming_tours=[]


driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
title=driver.title
print(title)
link=driver.get_cookies()
print(link)
driver.find_element(By.XPATH , "//a[text()='Live Scores']").click()
test=driver.find_element(By.XPATH,"//h1[text()='Live Cricket Score']")
message=test.text
print(message)
assert  message=="Live Cricket Score"
recent_tab=WebDriverWait(driver ,10).until(EC.element_to_be_clickable(driver.find_element(By.ID,"recent-tab")))
recent_tab.click()

cricket_series=driver.find_elements(By.XPATH,"//div[contains(@ng-show,'international-tab')]")
for series in cricket_series:
    team=series.text
    recent_tours.append(team)
print(f"recent tours and mathces are: {recent_tours}")
recent_tab=WebDriverWait(driver ,10).until(EC.element_to_be_clickable(driver.find_element(By.ID,"upcoming-tab")))
recent_tab.click()

upcoming_series=driver.find_elements(By.XPATH,"//h2[@class='cb-lv-grn-strip text-bold cb-lv-scr-mtch-hdr']")
for series in upcoming_series:
    up=series.text
    upcoming_tours.append(up)

print(f"upcoming tours and mathces are: {upcoming_series}")

schedule_tab=WebDriverWait(driver , 10).until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//a[text()='Schedule']")))
schedule_tab.click()

schedule_heading=driver.find_element(By.XPATH , "//h1[@class='cb-schdl-hdr cb-font-24 line-ht30']")
messsage_1=schedule_heading.text
time.sleep(3)
assert messsage_1=="Cricket Schedule"

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for 2 seconds to load content
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Fetch all the schedule dates
schedule_dates = driver.find_elements(By.XPATH, "//div[@class='cb-lv-grn-strip text-bold']")
for date in schedule_dates:
    date_text = date.text
    #print(date_text)

match = driver.find_elements(By.XPATH, "//a[@class='cb-col-33 cb-col cb-mtchs-dy text-bold']")
for date in match:
    match_day= date.text
    #print(match_day)


match_number = driver.find_elements(By.XPATH, "//div[contains(@class,'cb-mtchs-dy-vnu cb-adjst-lst')]")
for number in match_number:
    match_num= number.text
    print(match_num)

