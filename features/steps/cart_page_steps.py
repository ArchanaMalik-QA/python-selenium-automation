from selenium.webdriver.common.by import By
from behave import then
#from time import sleep

@then("Verify 'Your cart is empty ' message is shown")
def verify_cart_is_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains (text(),'Your cart is empty')]").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')

@then("Verify 'Your cart is having added items' message is shown")
def verify_cart_has_added_items(context):
    expected_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLinkQuantity']")
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartLinkQuantity']")
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')