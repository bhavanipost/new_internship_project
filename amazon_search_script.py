from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

sleep(5)

driver.get("https://www.amazon.com/")
sleep(5)

#input search text

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('treadmill')
sleep(5)

#click on search button

driver.find_element(By.ID,'nav-search-submit-button').click()
sleep(5)