import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class hostel():
    def test(self):
        path_val=os.environ.get('/usr/local/bin/')
        driver=webdriver.Chrome(path_val)
        driver.get("https://glexas.com/hostel/login")
        time.sleep(10)
        #driver.get("https://glexas.com/hostel/studentLeave")
        driver.find_element(By.XPATH,"//input[@class='form-control']").send_keys('studenttest')
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@type='password']").send_keys('studenttest')
        time.sleep(5)
        submit = driver.find_element(By.XPATH,"//button[@type='button']")
        submit.click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//a[@href='./dashboard']")

        leave = driver.find_element(By.XPATH,"//div[@class='d-flex align-items-center']")
        leave.click()
        time.sleep(4)

        add=driver.find_element(By.XPATH,"//button[@data-func='dt-add']")
        add.click()
        time.sleep(1)

        dropdown1=driver.find_element(By.ID,"leave_main_id")
        dd1=Select(dropdown1)
        dd1.select_by_visible_text("event visit")
        time.sleep(3)

        driver.find_element(By.XPATH,"//input[@class='form-control required']").send_keys('Vadodara')
        time.sleep(3)
 
        driver.find_element(By.XPATH,"//textarea[@class='form-control required']").send_keys('coding workshop')
        time.sleep(3)

        from_date = driver.find_element(By.XPATH,"//input[@min='2024-05-07']")
        from_date.send_keys('08052024')
        time.sleep(1)

        to_date = driver.find_element(By.XPATH,"//input[@id='to_date']")
        to_date.send_keys('09052024')
        time.sleep(1)

        from_time = driver.find_element(By.XPATH,"//input[@type='time']")
        from_time.send_keys('0500AM')
        time.sleep(1)

        to_time = driver.find_element(By.XPATH,"//input[@id='to_time']")
        to_time.send_keys('0900PM')
        time.sleep(1)

        submit1 = driver.find_element(By.XPATH,"//button[text()=' Submit ']")
        submit1.click()
        time.sleep(4)

        ok=driver.find_element(By.XPATH,"//button[text()='OK']")
        ok.click()
        time.sleep(1)



        

lease=hostel()
lease.test()


