#from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on Signin icon')
def click_signin(context):
    context.app.header.click_signin_icon()
    print('clicked on signin icon')

@when('User click on Signin Button')
def click_signin_button(context):
    context.app.signin_page.click_signin_btn()

@then('Verify Sign In form opened')
def verify_user_can_sign_in(context):
    context.app.signin_page.verify_user_can_sign_in()



