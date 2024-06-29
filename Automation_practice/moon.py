from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_carousel_items(driver, section_name):
    items = []

    try:
        # Navigate to the Noon website
        driver.get('https://www.noon.com/uae-en/')

        # Wait for the section to be visible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[text()='{section_name}']")))

        # Click on the section to expand the carousel
        section_element = driver.find_element(By.XPATH, f"//*[text()='{section_name}']")
        section_element.click()

        # Fetch all carousel items
        while True:
            carousel_items = driver.find_elements(By.XPATH, "//div[contains(@class, 'swiper-wrapper')]//*[contains(@class, 'swiper-slide')]")
            for item in carousel_items:
                items.append(item.text.strip())

            # Check if next arrow is visible
            next_arrow = driver.find_element(By.XPATH, "//div[contains(@class, 'swiper-button-next')]")
            if 'swiper-button-disabled' in next_arrow.get_attribute('class'):
                break  # Exit loop if next arrow is disabled

            # Click next arrow to load more items
            driver.execute_script("arguments[0].click();", next_arrow)
            time.sleep(2)  # Optional: Add a short delay for content to load

    except Exception as e:
        print(f"Error fetching {section_name} carousel items: {e}")

    return sorted(items)

# Example usage:
if __name__ == "__main__":
    # Initialize WebDriver (Chrome)
    driver = webdriver.Chrome()

    try:
        section_names = [
            "Recommended For You",
            "Sports shoes under 199 AED",
            "Top picks in laptops",
            "Limited time offers",
            "Bestselling fragrances"
        ]

        for section_name in section_names:
            carousel_items = fetch_carousel_items(driver, section_name)
            print(f"Carousel items for '{section_name}':")
            for item in carousel_items:
                print(item)
            print("-" * 50)  # Separator for clarity

    finally:
        # Close the WebDriver session
        driver.quit()
