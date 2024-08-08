from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.nike.com/in/w/sale-3yaep")

# Scroll to the bottom of the page to load all products
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)  # Adjust sleep time as necessary
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

# Initialize a list to collect the data
data = []

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')
product_cards = soup.find_all('div', class_='product-card__body')

# Extract data from each product card
for product in product_cards:
    try:
        link = product.find('a', class_='product-card__link-overlay').get('href')
        name = product.find('div', class_='product-card__titles').text.strip()
        subtitle = product.find('div', class_="product-card__subtitle").text.strip()
        sale_price = product.find('div', class_="product-price is--current-price css-1ydfahe").text.strip()
        full_price = product.find('div', class_="product-price in__styling is--striked-out css-0")
        full_price = full_price.text.strip() if full_price else 'N/A'  # Handle missing full price

        # Add the data to the list
        data.append({
            'Link': link,
            'Name': name,
            'Subtitle': subtitle,
            'Sale_Price': sale_price,
            'Full_Price': full_price
        })

    except Exception as e:
        print(f"Error processing product: {e}")
        continue

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv("Nike_data.csv", index=False)

# Close the WebDriver
driver.quit()
