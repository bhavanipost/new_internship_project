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

# open the url
driver.get('https://www.amazon.com/')

# # By ID
# driver.find_element(By.ID, 'nav-search-submit-button')
# driver.find_element(By.ID, 'nav-cart-count')
#
# # By XPATH
#
# # Tag and attribute
# driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
# driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
#
# # Multiple attributes
# driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")
#
# # By Xpath, text
# driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Any tag = *
#driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

# Contains
#driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
#driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")

# //parent[...]//child[...]
#driver.find_element(By.XPATH, "//div[@id='nav-belt']//input[@placeholder='Search Amazon']")

#driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()
driver.find_element(By.ID, 'nav-orders').click()

#Amazon logo, Search by Xpath
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']").is_displayed()

#Email Field,search by Xpath
driver.find_element(By.XPATH, "//input[@type='email']").is_displayed()


#Continue button,search by ID
driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#sign in button
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")


#driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")

#Conditions of use link,by Xpath
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#Privacy Notice link,by Xpath
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")

#Need help link,by Xpath
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()

sleep(3)

#Forget your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom']")

#Other issues with Sign_In link
driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/account-issues/ref=ap_login_with_otp_claim_collection?ie=UTF8']")

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

#Verify Sign in header
expected_text = 'Sign in'
actual_text = driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text
assert actual_text == expected_text, f'Expected {expected_text} but got {actual_text}'

#Verify email fieid present

driver.find_element(By.XPATH, "//input[@type='email']").send_keys("bhavanilink@gmail.com")

expected_text = 'bhavanilink@gmail.com'
actual_text = driver.find_element(By.XPATH, "//input[@type='email']").get_attribute("value")
assert actual_text == expected_text, f'Expected{expected_text} but got {actual_text}'

print('Test Passed')

length = driver.find_element(By.XPATH, "//input[@type='email']").get_attribute("id")
print("length is:" + length)




