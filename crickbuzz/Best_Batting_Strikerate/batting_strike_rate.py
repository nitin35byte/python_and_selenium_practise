import time
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
Odi_Highest_Run=[]

driver = webdriver.Chrome()
driver.get("https://www.cricbuzz.com/")
element_to_hover=WebDriverWait(driver , 10).until(EC.presence_of_element_located((By.XPATH,"//a[text()='Teams']")))
action=ActionChains(driver)
action.move_to_element(element_to_hover).perform()

select_team=WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"(//a[text()='India'])[1]")))
select_team.click()
driver.find_element(By.LINK_TEXT ,"Stats").click()

header=driver.find_element(By.XPATH,"//h1[text()='India National Cricket Team ']")
print(header.text)
time.sleep(5)

dropdown_element=driver.find_element(By.XPATH, "//strong[text()='Match Types']/..//select")
dropdown_element.click()
select=Select(dropdown_element)
select.select_by_visible_text("ODI")

driver.find_element(By.XPATH,"//a[normalize-space()= 'Best Batting Strike Rate']").click()

time.sleep(5)
most_run_by_players=driver.find_elements(By.CLASS_NAME,"cb-srs-stats-tr")
for run in most_run_by_players:
    runs=run.text
    Odi_Highest_Run.append(runs)
print(Odi_Highest_Run)


with open('odi_batting_strikerate.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["PLAYER", "MATCHES", "INNS", "RUNS", "AVG", "SR", "4s", "6s"])
    for row in Odi_Highest_Run:
        writer.writerow(row.split())


driver.quit()