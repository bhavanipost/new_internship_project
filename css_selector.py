from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
#driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(executable_path='/Users/bhavani/Desktop/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/")
sleep(5)

driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList').click()

driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()

sleep(5)

driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')

driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

driver.find_element(By.CSS_SELECTOR, '#ap_email')

driver.find_element(By.CSS_SELECTOR, '#ap_password')

driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be at least 6 characters.')]")



driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

driver.find_element(By.CSS_SELECTOR, '#continue')

driver.find_element(By.CSS_SELECTOR, '[href*="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use"]')

driver.find_element(By.CSS_SELECTOR, '[href*="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice"]')

driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age=0&openid.']")


#$$(".a-row.a-spacing-top-medium.a-size-small a[href*='condition_of_use']")
#$$("#legalTextRow a[href*='condition_of_use'] ")












