from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR,"[id*='addToCartButtonOrTextId'][data-test='chooseOptionsButton'][aria-label*='Add to cart']")
ADD_TO_CART_SIDE_NAV_BTN = (By.CSS_SELECTOR,"[data-test='fulfillment-cell-shipping']")
ADD_TO_CART_SIDE_NAV_BTN_SHIPPING = (By.CSS_SELECTOR,"[data-test='shippingButton']")
PRODUCT_NAME_SHOWN = (By.XPATH, "//div[@data-test='resultsHeading']")
PRODUCT_NAME = (By.CSS_SELECTOR,"[data-test='content-wrapper']h4")
CART_SIDE_NAV_CLOSE_BTN = (By.CSS_SELECTOR,"[aria-label='close']")


@then('Verify search results shown for {product}')
def verify_search_results(context, product):
    actual_result = context.driver.find_element(*PRODUCT_NAME_SHOWN).text
    assert product in actual_result, f'Expected text {product} not in actual {actual_result}'


@when('Add the product to cart')
def add_the_product_to_cart(context):
    context.driver.find_elements(*ADD_TO_CART_BTN)[0].click()

#   sleep(10)

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_elements(*PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to cart button from side navigation')
def confirm_add_to_cart_from_side_navigation(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_SIDE_NAV_BTN)).click()
    context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN).click()
    context.driver.find_element(*ADD_TO_CART_SIDE_NAV_BTN_SHIPPING).click()
    context.driver.find_element(*CART_SIDE_NAV_CLOSE_BTN).click()
    sleep(4)

