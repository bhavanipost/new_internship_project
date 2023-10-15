from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

service = Service(executable_path='/Users/bhavani/Desktop/Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-orders').click()

driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").is_displayed()

driver.find_element(By.XPATH, "//input[@type='email']").is_displayed()

driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").is_displayed()

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()

sleep(4)

driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")

driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

print('Test Passed')


driver.quit()
