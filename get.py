import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class setxpath():
    def test(self):
        path_val=os.environ.get('/usr/local/bin/')
        driver=webdriver.Chrome(path_val)
        driver.get("https://www.facebook.com/")
        driver.find_element(By.XPATH,"//input[@id='email']").send_keys('nisha.vipul1@gmail.com')
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='pass']").send_keys('nishashah')
        time.sleep(1)
        login = driver.find_element(By.XPATH,"//button[@type='submit']")
        login.click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[@id=':Riql9ad5bb9l5qq9papd5aq:']/span[1]")
        #window_handles = driver.window_handles
        #parent_handle=driver.current_window_handle
        #for i in window_handles:
        #    if i!=parent_handle:
        #        driver.switch_to.window(i)
        #        time.sleep(4)
        #        break
        


findbyxpath=setxpath()
findbyxpath.test()


