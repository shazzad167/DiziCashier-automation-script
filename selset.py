from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set Chrome options
options = webdriver.ChromeOptions()

# Provide the correct path to your ChromeDriver
driver_path = "C:/Users/Dizinova/OneDrive/Desktop/web driver/chromedriver-win64/chromedriver.exe"

# Initialize ChromeDriver
driver = webdriver.Chrome(options=options, service=webdriver.chrome.service.Service(driver_path))

try:
    # Open the login page
    driver.get("https://app.dizicashier.com/#!/")
    driver.maximize_window()

    # Log in
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Username"))).send_keys("shazzad167")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys("shazzad167")
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

    # Function to wait for an element
    def wait_for_element(xpath, timeout=10):
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    # Search and select the first product
    product_search_1 = wait_for_element("(//md-autocomplete[@placeholder='Search Item']//input)[1]")
    product_search_1.send_keys("item b")
    time.sleep(2)
    product_search_1.send_keys(Keys.ARROW_DOWN)
    product_search_1.send_keys(Keys.ENTER)

    # Search and select the second product
    product_search_2 = wait_for_element("(//md-autocomplete[@placeholder='Search Item']//input)[2]")
    product_search_2.send_keys("Item 55")
    time.sleep(2)
    #product_search_2.send_keys(Keys.ARROW_DOWN)
    #product_search_2.send_keys(Keys.ENTER)

    # Add a new product row and select the third product
    
    # Click on the Save button
    save_button = wait_for_element("//button[@ng-show='isValidsale'][text()='Save']")
    save_button.click()

    # Wait for the form submission
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='toast-message']"), "Sale has been saved successfully"))

    # Confirm success
    print("Sale with multiple products has been saved successfully.")

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser
    driver.quit()
