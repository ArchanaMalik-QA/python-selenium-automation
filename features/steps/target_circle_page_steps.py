from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify at least 10 benefit cells')
def verify_header_links(context):
    elements = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components']")
    print('\nFind element:')
    print(len(elements))
    assert len(elements) >= 10