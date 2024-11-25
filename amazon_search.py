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

#========================================================

#CSS Locators(Homework3)
#click on Create your Amazon account

driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()

sleep(5)

#I couldn't find (Amazon) image using CSS Selector so using XPATH
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")

#locating (Create Account)
driver.find_element(By.CSS_SELECTOR,"h1.a-spacing-small")

#locating customer name textbox
driver.find_element(By.CSS_SELECTOR,"#ap_customer_name")

#locating email id textbox
driver.find_element(By.CSS_SELECTOR,"#ap_email")

##locating password textbox
driver.find_element(By.CSS_SELECTOR,"#ap_password")

##locating alert for short password
driver.find_element(By.CSS_SELECTOR,"#auth-password-invalid-password-alert")

#locating re-enter password textbox
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")

#locating Create your Amazon account button
driver.find_element(By.CSS_SELECTOR,"input#continue.a-button-input")
#==================
#locating Condition of use link
driver.find_element(By.CSS_SELECTOR,"a[href*='condition_of_use?']")

#locating Privacy Notice link
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_register_notification_privacy_notice?']")

#locating Sign in Link
driver.find_element(By.CSS_SELECTOR,"a[href*='/ap/signin?openid.pape'].a-link-emphasis")


















driver.quit()
