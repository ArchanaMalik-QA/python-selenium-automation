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

driver.get('https://www.target.com')

# Search sign in
#driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3' and contains(text(),'Sign in')]").click()
sleep(3)
driver.find_element(By.XPATH, "//button[@type='button' and @data-test='accountNav-signIn']").click()
sleep(5)

# Verification:
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//h1/span[contains (text(),'Sign into your Target account')]").text

assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

# Verify an element present:
driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']")
#====================================Testcase to check if cart is empty======================
#Search for the cart icon
driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()
# Verification:
expected_result = 'Your cart is empty'
actual_result = driver.find_element(By.XPATH, "//h1[contains (text(),'Your cart is empty')]").text

assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test case passed')

# Verify an element present:
driver.find_element(By.XPATH, "//*[text()='Your cart is empty']")




