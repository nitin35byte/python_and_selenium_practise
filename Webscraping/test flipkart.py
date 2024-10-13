from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set location and file counter
location = 'pune'
file = 0

# Create a directory to store HTML files if it doesn't exist
output_dir = f"properties/{location}"
os.makedirs(output_dir, exist_ok=True)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the page
    for i in range(50):  # Limit to 50 pages
        driver.get(f"https://www.99acres.com/search/property/buy/{location}?city=19&preference=S&area_unit=1&res_com=R")
        time.sleep(5)  # Allow time for the page to load fully

        # Get all product elements
        products = driver.find_elements(By.CLASS_NAME, "PseudoTupleRevamp__tupleWrap")
        print(f'{len(products)} items found on page {i + 1}')

        for prod_index in range(len(products)):
            try:
                # Refetch the product element by index to avoid stale element reference
                products = driver.find_elements(By.CLASS_NAME, "PseudoTupleRevamp__tupleWrap")
                prod = products[prod_index]
                html_content = prod.get_attribute("outerHTML")

                # Save product HTML to files
                with open(f"{output_dir}/{location}_{file}.html", 'w', encoding='utf-8') as f:
                    f.write(html_content)
                file += 1
                time.sleep(2)  # Sleep to avoid overwhelming the server

            except Exception as e:
                print(f"Error processing product {prod_index + 1}: {e}")

        # Scroll to the bottom of the page to load more properties if available
        last_height = driver.execute_script('return document.body.scrollHeight')
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)  # Wait for the new content to load
            new_height = driver.execute_script('return document.body.scrollHeight')
            if new_height == last_height:
                print("Reached the end of the page")
                break
            last_height = new_height

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the browser after scraping
    driver.quit()
