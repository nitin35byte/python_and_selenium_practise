from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import calendar
import time

# Initialize the WebDriver (Chrome)
driver = webdriver.Chrome()

# Function to check if a date is a weekend (Saturday or Sunday)
def is_weekend(date):
    return date.weekday() in [5, 6]  # 5 is Saturday, 6 is Sunday

# Function to fetch weekend dates from the current month and future months
def fetch_weekend_dates():
    weekend_dates = []

    # Get today's date
    today = datetime.today()

    # Click on the date picker to open it
    date_picker_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".dateText"))
    )
    date_picker_button.click()

    # Function to collect weekend dates from the current view
    def collect_weekend_dates():
        dates_elements = driver.find_elements(By.CSS_SELECTOR, ".sc-jzJRlG.dPBSOp")
        for element in dates_elements:
            if 'current' in element.get_attribute('class'):  # Ensure the date is selectable
                date_text = element.text.strip()
                if date_text.isdigit():
                    date_value = int(date_text)
                    current_date = datetime(today.year, today.month, date_value)
                    if current_date >= today and is_weekend(current_date):
                        weekend_dates.append(current_date.strftime("%Y-%m-%d"))

    # Collect for the current month
    collect_weekend_dates()

    # Collect for future months (up to 11 months from now)
    for _ in range(11):
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".next"))
        )
        next_button.click()
        time.sleep(2)  # wait for the calendar to update
        collect_weekend_dates()

    return weekend_dates

# Function to count holidays in the given month and validate
def count_and_validate_holidays():
    # Get today's date and current month
    today = datetime.today()
    current_month = today.month
    current_year = today.year

    # Get the number of days in the current month
    num_days = calendar.monthrange(current_year, current_month)[1]

    # Count holidays (assuming they are marked in the calendar)
    holiday_count = len(driver.find_elements(By.CSS_SELECTOR, ".holiday"))

    # Validate the count of holidays
    print(f"Number of holidays in {today.strftime('%B %Y')}: {holiday_count}")

# Main execution
try:
    # Open RedBus website
    driver.get('https://www.redbus.in/')

    # Fetch and print weekend dates
    weekend_dates = fetch_weekend_dates()
    print("Weekend Dates:")
    for date in weekend_dates:
        print(date)

    # Validate holidays count
    count_and_validate_holidays()

finally:
    # Close the browser session
    driver.quit()
