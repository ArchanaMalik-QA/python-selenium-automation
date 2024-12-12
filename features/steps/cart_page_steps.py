from selenium.webdriver.common.by import By
from behave import then, when
#from time import sleep


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()

@then("Verify 'Your cart is empty ' message is shown")
def verify_cart_is_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[contains (text(),'Your cart is empty')]").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    print('Test case passed')

@then("Verify cart has {amount} item(s)")
def verify_cart_has_added_items(context,amount):
    cart_summary = context.driver.find_element(By.CSS_SELECTOR,"[data-test='cart-summary-item-count']")
    assert f'{amount} items' in cart_summary, f'Expected {amount} items but got {cart_summary}'
    print('cart_summary')
    print('Test case passed')