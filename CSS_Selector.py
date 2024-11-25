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

#CSS
driver.find_element(By.ID,"twotabsearchtextbox")
#CSS, by ID
driver.find_element(By.CSS_SELECTOR,'twotabsearchtextbox')
#CSS, by ID and tag
driver.find_element(By.CSS_SELECTOR,'input#twotabsearchtextbox')

#CSS, by class
driver.find_element(By.CSS_SELECTOR,'.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR,'.nav-progressive-attribute.nav-input')
#CSS, by tag and class
driver.find_element(By.CSS_SELECTOR,'input.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR,'input#twotabsearchtextbox.nav-progressive-attribute.nav-input')

#CSS by attributes (selector syntax: tag[attribute=value])
driver.find_element(By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav-cs-bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav-cs-bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav-cs-bestsellers']")
#CSS selector attribute with class
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav-cs-bestsellers']")

#CSS selector attribute partial match(* to use for partial match...works like contains in Xpath)[example popular filters in targert site]
driver.find_element(By.CSS_SELECTOR, "a[href*='nav-cs-bestsellers']")
#keep in mind, you can access class as attributes.
driver.find_element(By.CSS_SELECTOR, "[class*='styles_baseCell'][class*='styles_cellSkinny']")

# by CSS selector , from parent node =>to child
driver.find_element(By.CSS_SELECTOR, "[data-module-type='ProductListGrid'] h2")