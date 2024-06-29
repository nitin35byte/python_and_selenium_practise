from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def is_weekend(day_element):
    day_class = day_element.get_attribute('class')
    return 'weekend' in day_class

def navigate_to_date(target_month, target_year, target_day):
    while True:
        # Get the current month and year displayed in the calendar
        year_month_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='DayNavigator__CalendarHeader-qj8jdz-1 fxvMrr']//div[2]"))
        )
        year_month = year_month_element.text.strip()
        print(year_month)

        current_month = year_month.split()[0]
        current_year = year_month.split()[1]

        # Print all weekend dates for the current month
        days_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'DayNavigator__Day')]//span[@class='DayNavigator__DayNumber-sc-1kr1trj-3 dQqXFA']")
        for day_element in days_elements:
            day_text = day_element.text
            if day_text.isdigit() and is_weekend(day_element):
                print(f"Weekend Date: {current_month} {day_text}, {current_year}")

        # Check if the current month and year match the target month and year
        if current_month == target_month and int(current_year) == target_year:
            # Click the target day
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//span[normalize-space()='{target_day}']"))
            ).click()
            break
        else:
            # Click the next month button
            next_month_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='DayNavigator__CalendarHeader-qj8jdz-1 fxvMrr']//div[3]"))
            )
            next_month_button.click()
            time.sleep(1)  # Wait for the calendar to update

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the Goibibo website
driver.get("https://www.redbus.in/")

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time if necessary to handle any initial loading or popups

# Click the 'Departure' element to open the date picker
departure_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Departure']"))
)
departure_element.click()

# Define the target date
target_month = "June"
target_year = 2025
target_day = 4

# Navigate to the target date and print all weekend dates
navigate_to_date(target_month, target_year, target_day)

# Optional: Add more interactions here

# Close the browser
driver.quit()
