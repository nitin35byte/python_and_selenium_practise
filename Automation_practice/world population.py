from selenium import webdriver
import time
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Initialize WebDriver (Chrome)
driver = webdriver.Chrome()
# driver.get('https://www.worldometers.info/world-population/')
# ##driver.find_element(By.XPATH)
# title=driver.title
# print(title)

##world_population=driver.find_element(By.XPATH,"//span[@rel='births_today']").text
##print(world_population)
try:
    # Function to fetch and print world population statistics
    def fetch_world_population():
        driver.get('https://www.worldometers.info/world-population/')

        # Fetch current world population
        world_population = driver.find_element(By.XPATH,"//span[@rel='current_population']").text
        print(world_population)

        # Fetch today's births, deaths, and population growth

        today_births = driver.find_element(By.XPATH,"//span[@rel='births_today']").text
        print(today_births)
        today_deaths = driver.find_element(By.XPATH,"//span[@rel='dth1s_today']").text
        print(today_deaths)
        today_growth = driver.find_element(By.XPATH,"//span[@rel='absolute_growth']").text
        print(today_growth)
        # Fetch this year's births, deaths, and population growth
        this_year_births = driver.find_element(By.XPATH,"//span[@rel='births_this_year']").text
        this_year_deaths = driver.find_element(By.XPATH,"//span[@rel='dth1s_this_year']").text
        this_year_growth = driver.find_element(By.XPATH,"//span[@rel='absolute_growth_year']").text

        # Print the fetched statistics
        print(f"Current World Population: {world_population}")
        print(f"Today's Births: {today_births}, Deaths: {today_deaths}, Growth: {today_growth}")
        print(f"This Year's Births: {this_year_births}, Deaths: {this_year_deaths}, Growth: {this_year_growth}")
        print("-" * 30)  # Separator for clarity


    # Continuous loop to fetch statistics every few seconds
    while True:
        fetch_world_population()
        time.sleep(20)  # Wait for 20 seconds before fetching again

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver session
    driver.quit()
