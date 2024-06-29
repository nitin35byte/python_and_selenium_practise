# a =[]
# b = []
# if a in b:
#      pass
# else:
#      fail

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the Amazon India homepage
    driver.get("https://www.amazon.in")

    # Wait for the search box to be present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )

    # Enter the search term and submit
    search_box.send_keys("laptop")
    search_box.submit()

    # Wait for the search results to load
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'results')]"))
    )

    # Click on the first item in the search results
    first_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results_1']//h2/a"))
    )
    first_item.click()

    # Wait for the 'Add to Cart' button to be present and click it
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Add to Cart']"))
    )
    add_to_cart_button.click()

    print("Item added to cart successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the driver
    driver.quit()
