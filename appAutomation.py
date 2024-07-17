from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the Appium driver
desired_caps = {
    'platformName': 'Android',
    'platformVersion': 'YOUR_ANDROID_VERSION',
    'deviceName': 'YOUR_DEVICE_NAME',
    'appPackage': 'com.facebook.katana',
    'appActivity': 'com.facebook.katana.LoginActivity',
    'automationName': 'UiAutomator2'
}

# Appium server URL
appium_url = 'http://localhost:4723/wd/hub'

# Initialize the driver
driver = webdriver.Remote(appium_url, desired_caps)

# Wait for the login button to be visible
login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'login_button')))

# Click the login button
login_button.click()

# Enter username and password
username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'm_login_email')))
username_field.send_keys('YOUR_FACEBOOK_USERNAME')

password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'm_login_password')))
password_field.send_keys('YOUR_FACEBOOK_PASSWORD')

# Click the login button
login_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'login')))
login_button.click()
