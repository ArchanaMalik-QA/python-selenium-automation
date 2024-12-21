from behave import given, when, then


@given('Open sign in page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()
    context.app.header.click_signin_icon()
    context.app.signin_page.click_signin_btn()


# @given('Store original window')
# def store_original_window(context):
#     context.original_window = context.app.target_app_page.get_current_window_handle()


@when('Click on Target terms and conditions link')
def click_tandc_link(context):
    context.app.target_app_page.click_tandc_link()


@when('Switch to the newly opened window')
def switch_window(context):
    # print('All windows', context.driver.window_handles) # [Win1, Win2, ...]
    # context.driver.switch_to.window(context.driver.window_handles[1])
    context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_TandC_opened(context):
    context.app.terms_and_conditions_page.verify_TandC_opened()


@then('Close New Window page')
def close_page(context):
    context.app.terms_and_conditions_page.close()


@then('Return to original window SignIn')
def return_to_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)