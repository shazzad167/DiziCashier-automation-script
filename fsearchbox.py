from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time 
from selenium.webdriver.common.keys import Keys  
# Set Chrome options
options = webdriver.ChromeOptions()

# Provide the correct path to your ChromeDriver
driver_path = "C:/Users/Dizinova/OneDrive/Desktop/web driver/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(options=options, service=Service(driver_path))


# Function to log in to the application
def login_to_dizicashier():
    driver.get("https://app.dizicashier.com/#!/")
    driver.maximize_window()

    # Wait for the login fields to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Username")))
    driver.find_element(By.NAME, "Username").send_keys("shazzad167")  # Replace with your username
    driver.find_element(By.NAME, "Password").send_keys("shazzad167")  # Replace with your password

    # Click the login button
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()

    # Wait until the dashboard or another element confirms login
    time.sleep(7)


# Function to extract stock report data
def extract_stockreport_data():
    driver.get("https://app.dizicashier.com/#!/report/stockreport")
    driver.execute_script("document.body.style.zoom='90%'")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Warehouse']")))

    # Click on the Warehouse dropdown and select the desired warehouse
    warehouse_dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/input")
    warehouse_dropdown.click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'shatkania')]")))
    warehouse_option = driver.find_element(By.XPATH, "//div[contains(text(), 'shatkania')]")
    warehouse_option.click()

    # Wait for iframe to load and switch to it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # Interact with the search box and find button
    search_box_xpath = "/html/body/div/form/div[2]/div/table/tbody/tr[4]/td/div[1]/div/div[7]/table/tbody/tr/td[1]/input"
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_box_xpath)))
    search_box.clear()
    search_value = "item 441"
    search_box.send_keys(search_value)

    # Locate and click the Find button
      # Simulate pressing the Enter key
    search_box.send_keys(Keys.ENTER)

    # Wait for results to load
    time.sleep(5)

    # Switch to iframe again if necessary
    driver.switch_to.default_content()  # Ensure switching back before accessing the iframe again
    iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    driver.switch_to.frame(iframe)

    # Extract product details
    product_xpath = "/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[15]/td[3]/div/div/span"
    quantity_xpath = "/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[15]/td[6]/div/div"
    
    product = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, product_xpath))).text
    quantity = driver.find_element(By.XPATH, quantity_xpath).text

    return [{"Field Name": product, "Value": quantity}]


# Function to save data to a CSV file
def save_to_csv(data, file_name="box.csv"):
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Field Name", "Value"])
        writer.writeheader()
        writer.writerows(data)


# Main workflow
try:
    login_to_dizicashier()
    stock_report_data = extract_stockreport_data()
    save_to_csv(stock_report_data)
    print("Data has been successfully saved to CSV.")
finally:
    driver.quit()
