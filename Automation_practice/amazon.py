import time
import  pandas as pd
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def comparing_product_from_excel():
    # Set up the Selenium WebDriver with options for headless browsing and performance
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    title=driver.title
    print(title)

    link=driver.find_elements(By.TAG_NAME,"a")
    prodcut_links=[]
    for links in  link:

        prodcut_links.append(links.get_attribute("href"))
    #print(prodcut_links)
    ##print(len(prodcut_links))

    for product in prodcut_links:
        pass
        #print(product)

    driver.find_element(By.ID,"twotabsearchtextbox").send_keys("iphone15")
    driver.find_element(By.ID,"nav-search-submit-button").click()
    add_cart=driver.find_elements(By.XPATH,"//button[@type='button']")
    index= 0
    for button in add_cart:
        try:
            button.click()
            index +=1
            time.sleep(1)  # Add a short delay to ensure each click is registered
        except Exception as e:
            print(f"An error occurred: {e}")
    print(f"product count is :",index)
    try:
        cart_element = driver.find_element(By.ID, "nav-cart-text-container")
        driver.execute_script("arguments[0].scrollIntoView(true);", cart_element)
        time.sleep(1)  # Allow time for scrolling
        driver.execute_script("arguments[0].click();", cart_element)
        time.sleep(5)  # Wait for the cart page to load
    except Exception as e:
        print(f"An error occurred while navigating to the cart: {e}")

    # try:
    #     driver.find_element(By.ID,"nav-cart-text-container").click()
    #     time.sleep(5)
    # except Exception as e:
    #     print(f"An error occurred while navigating to the cart: {e}")

    try:
        cart_items = []
        product_count=driver.find_element(By.ID,"nav-cart-count")
        cart_items.append(product_count.get_attribute("aria-label"))
        print(cart_items)
    except Exception as e:
        print(f"An error occurred while retrieving the product count: {e}")


    cart_items = []
    product_names = driver.find_elements(By.XPATH, "//span[@class='a-truncate-cut']")
    for product in product_names:
        cart_items.append(product.text)
    print(cart_items)
    """
    The method is created to add into excel and save as xlsx in format
    """
    # output_file = 'amazon_cart_items.xlsx'
    # # Create a DataFrame from the extracted items
    # df = pd.DataFrame({'Item Name': cart_items})
    #
    # # Export the DataFrame to Excel
    # df.to_excel(output_file, index=False)
    #
    # print(f"Extracted items from Amazon cart saved to '{output_file}'.")

    ##Compare
    excel_file_path=r'input file path'
    df = pd.read_excel('amazon_cart_items.xlsx')
    excel_item= df['Item Name'].tolist()
    print(f"item in excel:",excel_item)
    print(len(df))


    results = {'Item': [], 'Status': []}

    for item in excel_item:
        if item in cart_items:
            print("Test Case pass")
    else:
        print("test case fail")

comparing_product_from_excel()

## firs i will read scve
## then i will conver data to list
## i have add to card item which i have stored in varibale
## now will a run a loop anditerate throyugh element
