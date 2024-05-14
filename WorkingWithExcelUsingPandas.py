import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path_val=os.environ.get('/usr/local/bin/')
driver=webdriver.Chrome(path_val)
driver.maximize_window()
driver.get("https://glexas.com/hostel/login")
time.sleep(20)

df = pd.read_excel("/Users/nilayshah/Desktop/paths.xlsx", sheet_name=['Main','Web'])
MainSheet = df["Main"]
WebSheet = df["Web"]

MRows = MainSheet.shape[0]
MCols = MainSheet.shape[1]
Wrows = WebSheet.shape[0]



def lease(Id, Wrows, WebSheet):
    
    for rows in range(2, Wrows + 1):

        WTitle = WebSheet.iloc[rows - 1, 1]
        if(WTitle == Id):
            path = WebSheet.iloc[rows - 1, 3]
            val = WebSheet.iloc[rows - 1, 4]

            if val == 0:
                driver.find_element(By.XPATH, path).click()   
                time.sleep(5)

            else:
                if val == "event visit":
                    time.sleep(5)
                    title = Select(driver.find_element(By.XPATH, path))
                    title.select_by_visible_text(val)
                    time.sleep(5)
                else:
                    driver.find_element(By.XPATH, path).send_keys(val)
                    time.sleep(3)
        
        else:
            continue



for row in range(1, MRows+1):
    Id = MainSheet.iloc[row - 1, 1]
    lease(Id, Wrows, WebSheet)
