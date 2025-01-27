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
    driver.get("https://app.dizicashier.com/#!/")
    driver.maximize_window()

    # Enter username and password
    driver.find_element(By.NAME, "Username").send_keys("shazzad167")  # Replace with your username
    driver.find_element(By.NAME, "Password").send_keys("shazzad167")  # Replace with your password

    # Click login
    driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()
    time.sleep(7)  # Wait for the page to load
def extract_stockreport_data():
    driver.get("https://app.dizicashier.com/#!/report/stockreport")
    driver.execute_script("document.body.style.zoom='90%'")
    time.sleep(6)

    # Click on the Warehouse dropdown
    warehouse_dropdown = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/input")
    warehouse_dropdown.click()
    time.sleep(1)  # Allow the dropdown to appear

    # Select the desired warehouse option
    warehouse_option = driver.find_element(By.XPATH, "//div[contains(text(), 'shatkania')]")
    warehouse_option.click()
    time.sleep(6)  # Wait for generation
    iframe = driver.find_element(By.TAG_NAME, "iframe")  # Locate iframe by tag name (or use a more specific selector)
    driver.switch_to.frame(iframe)
    search_box_xpath = "/html/body/div/form/div[2]/div/table/tbody/tr[4]/td/div[1]/div/div[7]/table/tbody/tr/td[1]/input"
    search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_box_xpath))
        )
    search_value = "item 441"
    search_box.clear()
    search_box.send_keys(search_value)

        # Locate the Find button and click it
    #find_button_xpath = "/html/body/div/form/div[2]/div/table/tbody/tr[4]/td/div[1]/div/div[7]/table/tbody/tr/td[3]/a"
                         
    #find_button = WebDriverWait(driver, 10).until(
            #EC.element_to_be_clickable((By.XPATH, find_button_xpath))
        #)
    #find_button.click()
    find_button = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div/table/tbody/tr[4]/td/div[1]/div/div[7]/table/tbody/tr/td[3]/a")
    driver.execute_script("arguments[0].click();", find_button)
    time.sleep(8) 
    
    iframe = driver.find_element(By.TAG_NAME, "iframe")  # Locate iframe by tag name (or use a more specific selector)
    driver.switch_to.frame(iframe)
    product = driver.find_element(By.XPATH, "/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[15]/td[3]/div/div/span").text
    quantity = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div/table/tbody/tr[5]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[15]/td[6]/div/div").text
    return [
        {"Field Name": product, "Value": quantity}
        
    ]
def save_to_csv(data, file_name="box.csv"):
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Field Name", "Value"])
        writer.writeheader()
        writer.writerows(data)

# Main workflow
try:
    login_to_dizicashier()

    # Extract data from both pages
   
    
    stock_report_data = extract_stockreport_data()

    # Combine data and save to CSV
    all_data =  stock_report_data
    save_to_csv(all_data)

    print("Data has been successfully saved to CSV.")
finally:
    driver.quit()
