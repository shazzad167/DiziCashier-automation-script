from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support import expected_conditions as EC
import time
def wait_for_element(by, value):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
# Set Chrome options
options = webdriver.ChromeOptions()

# Provide the correct path to your ChromeDriver
driver_path = "C:/Users/Dizinova/OneDrive/Desktop/web driver/chromedriver-win64/chromedriver.exe"

# Initialize ChromeDriver
driver = webdriver.Chrome(options=options, service=webdriver.chrome.service.Service(driver_path))

try:
    # Open the login page
    driver.get("https://dev.dizicashier.com/#!/")
    driver.maximize_window()

    # Log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Username"))).send_keys("mohaimin123")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys("12345")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='LOGIN']"))).click()

    # Wait for the dashboard to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnGroupDropQuickButton")))

    # Click on the "Add New" button
    add_new_button = driver.find_element(By.ID, "btnGroupDropQuickButton")
    add_new_button.click()

    # Wait for the dropdown to appear
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Make Sale']"))).click()

    # Wait for the Make Sale page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//md-autocomplete[@placeholder='Search Customer']//input")))

    # Search and select the customer
    customer_search_input = driver.find_element(By.XPATH, "//md-autocomplete[@placeholder='Search Customer']//input")
    customer_search_input.send_keys("Abdullah")
    time.sleep(2)
    customer_search_input.send_keys(Keys.ARROW_DOWN)
    customer_search_input.send_keys(Keys.ENTER)

    # Wait for the customer to be selected
    time.sleep(2)
    def wait_for_element(xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Search and select the first product
    product_search_1 = wait_for_element("(//md-autocomplete[@placeholder='Search Item']//input)[1]")
    product_search_1.send_keys("item b")
    time.sleep(2)
    def wait_for_element(by, value):
        return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, value)))
    
# Correct XPaths
    quantity_xpath = "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/form/div[3]/table/tbody/tr[1]/td[2]/div/input"
    price_xpath = "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/form/div[3]/table/tbody/tr[1]/td[3]/div/input"

# Step 1: Wait for the Quantity input field and interact with it
    try:
        quantity_input = wait_for_element(By.XPATH, quantity_xpath)  # Wait until it's clickable
        quantity_input.clear()  # Clear the existing value
        quantity_input.send_keys("3")  # Set the desired quantity
        time.sleep(3)
        print("Successfully set quantity.")
    except Exception as e:
        print(f"An error occurred with the Quantity field: {e}")

# Step 2: Wait for the Unit Price input field and interact with it
    try:
        price_input = wait_for_element(By.XPATH, price_xpath)  # Wait until it's clickable
        price_input.clear()  # Clear the existing value
        price_input.send_keys("750")  # Set the desired unit price
        time.sleep(4)
        print("Successfully set unit price.")
    except Exception as e:
       print(f"An error occurred with the Unit Price field: {e}")

    

    # Confirm success
  #  product_search_2 = wait_for_element("(//md-autocomplete[@placeholder='Search Item']//input)[2]")
   # product_search_2.send_keys("Item 55")
    #time.sleep(2)
    # Wait for the quantity input field to appear and click on it
    # Wait for the quantity input field to appear and click on it
    #quantity_input2 = wait_for_element(By.XPATH, "//input[@id='sale_ItemId']")  # XPath targeting the input by ID
    #quantity_input2.click()  # Click to focus on the input field

# Wait briefly for the field to become ready
    #time.sleep(1)  # Optional, adjust this delay if needed

# Change the quantity value (e.g., set to 2)
    #quantity_input2.send_keys("3")  # This will replace the existing value with the new one

# Wait for the unit price input field to appear and click on it
    #price_input2 = wait_for_element(By.XPATH, "//input[@id='sale_item_PricePerUnit']")  # XPath targeting the input by ID
    #price_input2.click()  # Click to focus on the input field

# Wait briefly for the field to become ready
    #time.sleep(1)  # Optional, adjust this delay if needed

# Change the unit price value (e.g., set to 150)
    #price_input.send_keys("1250")  # This will replace the existing value with the new one



    # Click on the Save button
    # Wait for and click the Save button
    def wait_for_element(driver, by, value, timeout=10):
         return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

    try:
        save_button = wait_for_element(driver, By.XPATH, "//button[@ng-show='isValidsale'][text()='Save']")  # Corrected function call
        save_button.click()  # Click the Save button

    # Wait for the success message
        WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, "//div[@class='toast-message']"), "Sale has been saved successfully"))

    # Confirm success
        print("Sale with modified quantity and price has been saved successfully.")
    except Exception as e:
        print(f"An error occurred with the Save button: {e}")


except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser
    driver.quit()
