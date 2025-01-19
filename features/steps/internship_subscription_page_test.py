from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open the main page https://soft.reelly.io')
def open_main_page(context):
    context.app.internship_main_page.open_main_page()


@given('Log in to the page')
def login(context):
    context.app.internship_main_page.login_add()
    sleep(3)

@when('Click on settings option')
def click_settings_button(context):
    context.app.internship_main_page.click_settings_button()
#
@when('Click on Subscription & payments option')
def  click_subscription_and_payments(context):
    context.app.internship_settings_page.click_subscription_and_payments()
#
@then('Verify the right page opens')
def verify_page(context):
    context.app.internship_subscription_page.verify_page()

@then('Verify title “Subscription & payments” is visible')
def verify_header(context):
    context.app.internship_subscription_page.verify_header()
#
@then('Verify “back” and “upgrade plan” buttons are available')
def verify_back_and_upgrade_plan_buttons(context):
    context.app.internship_subscription_page.verify_back_and_upgrade_plan_buttons()