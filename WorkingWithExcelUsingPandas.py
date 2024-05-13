import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

# Load data from Excel file using pandas
df = pd.read_excel("EXCELFILE/selenium_prac.xlsx", sheet_name='Sheet1')

rows = df.shape[0]  # Total number of rows in the DataFrame
#total_cols = df.shape[1]  # Total number of columns in the DataFrame

print(rows)
#print(total_cols)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(10)

for r in range(2, rows+1):
    path = df.iloc[r - 1, 3]  # Assuming the path is in the 4th column (Python index starts from 0)
    val = df.iloc[r - 1, 4]   # Assuming the value is in the 5th column (Python index starts from 0)

    if val == 0:
        print("HII you are in if statement")
        driver.find_element(By.XPATH, path).click()
        time.sleep(2)
    else:
        if val == "event visit":
            title = Select(driver.find_element(By.XPATH, '//*[@id="leave_main_id"]'))
            title.select_by_visible_text("event visit")
            time.sleep(5)
        else:
            print("HII you are in else statement")
            driver.find_element(By.XPATH, path).send_keys(val)
            time.sleep(2)

time.sleep(10)
