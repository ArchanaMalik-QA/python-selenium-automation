from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://target.com/')

@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(10)


@when('Add the product to cart')
def add_the_product_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"#addToCartButtonOrTextIdFor13010225[data-test='chooseOptionsButton']").click()
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR,"#addToCartButtonOrTextIdFor13010225[data-test='orderPickupButton']").click()
    sleep(10)
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='modal-drawer-previous-button']").click()
    context.driver.find_element(By.CSS_SELECTOR,"[aria-label='close']").click()
    sleep(5)

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then('Verify at least 1 header link is shown')
def verify_header_links(context):
    el = context.driver.find_element(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind element:')
    print(el)


@then('Verify {expected_amount} header links are shown')
def verify_header_links_amount(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    print('\nFind elements:')
    print(links)
    print(type(len(links)))

    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'