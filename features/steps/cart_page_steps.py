from selenium.webdriver.common.by import By
from behave import given, when, then

CART_SUMMARY_COUNT = (By.CSS_SELECTOR,"[data-test='cart-summary-item-count']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
CART_IS_EMPTY = (By.XPATH, "//h1[contains (text(),'Your cart is empty')]")


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')


@then("Verify 'Your cart is empty ' message is shown")
def verify_cart_is_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(*CART_IS_EMPTY).text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@then("Verify cart has {amount} item(s)")
def verify_cart_has_added_items(context,amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY_COUNT)
    assert f'{amount} items' in cart_summary, f'Expected {amount} items but got {cart_summary}'


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE)[0].text
    print(f'Actual product in cart name: {actual_name}')
    print(f'Product name stored earlier: {context.product_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"