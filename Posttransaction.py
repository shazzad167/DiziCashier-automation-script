from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

# Set Chrome options
options = webdriver.ChromeOptions()

# Provide the correct path to your ChromeDriver
driver_path = "C:/Users/Dizinova/OneDrive/Desktop/web driver/chromedriver-win64/chromedriver.exe"
driver = webdriver.Chrome(options=options, service=Service(driver_path))

# Function to log in to the application
def login_to_dizicashier():
    driver.get("https://dev.dizicashier.com/login")
    driver.maximize_window()

    # Enter username and password
    driver.find_element(By.NAME, "Username").send_keys("mohaimin123")  # Replace with your username
    driver.find_element(By.NAME, "Password").send_keys("12345")  # Replace with your password

    # Click login
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(7)  # Wait for the page to load

# Function to extract data from the accounts page
def extract_accounts_data():
    driver.get("https://dev.dizicashier.com/#!/accounts")
    time.sleep(8)

    # Extract Petty Cash and its value
    petty_cash_name = driver.find_element(By.XPATH, "//html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/span").text
    petty_cash_value = driver.find_element(By.XPATH, "//html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/span").text

    # Extract Accounts Receivable and its value
    accounts_receivable_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[1]/span").text
    accounts_receivable_value = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[4]/div[2]/div[1]/div[2]").text

    return [
        {"Field Name": petty_cash_name, "Value": petty_cash_value},
        {"Field Name": accounts_receivable_name, "Value": accounts_receivable_value},
    ]

# Function to extract stock data
def extract_stock_data():
    driver.get("https://dev.dizicashier.com/#!/stocks?page=1&sort=Name-asc&ListFilter.Quantity=%3E0&ListFilter.ItemCategoryIds=")
    time.sleep(8)

    # Extract product name and stock quantity
    product_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[2]/td[1]").text
    product_quantity = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[2]/td[4]/span").text
    product_namee = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[22]/td[1]").text
    product_quantityy = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[22]/td[4]/span").text

    return [
        {"Field Name": product_name, "Value": product_quantity},
        {"Field Name": product_namee, "Value": product_quantityy}
    ]

# Function to extract stock report data
def extract_stockreport_data():
    driver.get("https://dev.dizicashier.com/#!/report/stockreport")
    time.sleep(6)

    # Click on the Warehouse dropdown
    warehouse_dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/input")
    warehouse_dropdown.click()
    time.sleep(1)  # Allow the dropdown to appear

    # Select the desired warehouse option
    warehouse_option = driver.find_element(By.XPATH, "//div[contains(text(), 'Gulshan')]")
    warehouse_option.click()
    time.sleep(8)  # Wait for the stock report to load
    iframe = driver.find_element(By.TAG_NAME, "iframe")  # Locate iframe by tag name (or use a more specific selector)
    driver.switch_to.frame(iframe)
    # Check if the stock report has loaded and extract data
    
    stock_value = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/table/tbody/tr[2]/td[9]/div/div").text
    total_stock_amount = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/table/tbody/tr[13]/td[9]/div/div").text

    return [
            {"Field Name": stock_value, "Value": total_stock_amount}
        ]
   
# Function to save data to CSV
def save_to_csv(data, file_name="preoutput.csv"):
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Field Name", "Value"])
        writer.writeheader()
        writer.writerows(data)

# Main workflow
try:
    login_to_dizicashier()

    # Extract data from both pages
    accounts_data = extract_accounts_data()
    stock_data = extract_stock_data()
    stock_report_data = extract_stockreport_data()

    # Combine data and save to CSV
    all_data = accounts_data + stock_data + stock_report_data
    save_to_csv(all_data)

    print("Data has been successfully saved to CSV.")
finally:
    driver.quit()
