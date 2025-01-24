from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to wait for elements to become clickable
def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

# Set Chrome options
options = webdriver.ChromeOptions()

# Provide the correct path to your ChromeDriver
driver_path = "C:/Users/Dizinova/OneDrive/Desktop/web driver/chromedriver-win64/chromedriver.exe"

# Initialize ChromeDriver
driver = webdriver.Chrome(options=options, service=webdriver.chrome.service.Service(driver_path))

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
customer_search_input.send_keys("Ahanaf")
time.sleep(2)
customer_search_input.send_keys(Keys.ARROW_DOWN)
customer_search_input.send_keys(Keys.ENTER)

# Wait for the customer to be selected
time.sleep(2)

# Search and select the first product
product_search_1 = wait_for_element(driver, By.XPATH, "(//md-autocomplete[@placeholder='Search Item']//input)[1]")
product_search_1.send_keys("demo last")
time.sleep(2)

# Correct XPaths
quantity_xpath = "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/form/div[3]/table/tbody/tr[1]/td[2]/div/input"
price_xpath = "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/form/div[3]/table/tbody/tr[1]/td[3]/div/input"

# Set quantity
quantity_input = wait_for_element(driver, By.XPATH, quantity_xpath)
quantity_input.clear()
quantity_input.send_keys("3")
time.sleep(3)
print("Successfully set quantity.")

# Set unit price
price_input = wait_for_element(driver, By.XPATH, price_xpath)
price_input.clear()
price_input.send_keys("750")
time.sleep(4)
print("Successfully set unit price.")

# Click on the Save button
save_button = wait_for_element(driver, By.XPATH, "//button[@ng-show='isValidsale'][text()='Save']")
save_button.click()

# Wait for the success message
WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//div[@class='toast-message']"), "Sale has been saved successfully"))

# Confirm success
print("Sale with modified quantity and price has been saved successfully.")

# Close the browser
driver.quit()
