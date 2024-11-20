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

driver.get('https://www.amazon.com')
# Enter Capta Manually within 20seconds
sleep(10)

#click on signin link
driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']").click()
sleep(5)

# Practice with locators.:
# Search Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#Search Email Field
driver.find_element(By.XPATH, "//input[@id='ap_email']")

#Search for continue Button
driver.find_element(By.XPATH, "//input[@id='continue']")

#Search for Conditions of use link and Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(text(),'Conditions of Use')]")
driver.find_element(By.XPATH, "//a[contains(text(),'Privacy Notice')]")

#Search for Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt' and contains(text(),'Need help?')]")

#click on Need help link to expand for other elements to be searched
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt' and contains(text(),'Need help?')]").click()
sleep(5)

#search for Forgot your password link
driver.find_element(By.XPATH, "//a[@id='auth-fpp-link-bottom' and contains(text(),'Forgot your password?')]")

#search for Other issues with Sign-In link
driver.find_element(By.XPATH, "//a[@id='ap-other-signin-issues-link']")

#search for Create your amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")

driver.quit()
