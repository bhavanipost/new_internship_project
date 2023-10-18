from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open the Reelly main page')
def open_login_page(context):
    context.app.login_page.login_pages()


@when('Login to the Reelly page')
def login_to_webpage(context):
    context.app.login_page.click_on_signin_link()
    sleep(2)
    context.app.login_page.input_email("bhavani_post@yahoo.com")
    sleep(2)
    context.app.login_page.password_input_field("QAAUTO")
    sleep(2)
    context.app.login_page.click_continue()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep((3))


@then("Click on Get a free subscription")
def click_free_subscription(context):
    context.app.main_web_page.free_subscription_click()


# @then("Click on Get a free subscription")
# def click_free_subscription(context):
#     context.driver.wait.until(
#         EC.visibility_of_element_located(FREE_SUBSCRIPTION),
#         message='free subscription btn not clickable'
#     ).click()
#     context.app.main_web_page.free_subscription_click()


@then("Switch to the new tab")
def reelly_new_page_open(context):
    context.app.get_free_subscription_page.open_new_reelly_page()


@then('Verify the {text} in the new tab')
def verify_free_subscription_text(context, text):
    context.app.get_free_subscription_page.verify_subscription_text(text)




