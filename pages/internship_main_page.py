from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class InternshipMainPage(BasePage):
    EMAIL_TAB=(By.ID, 'email-2')
    PASSWORD_TAB=(By.ID, 'field')
    CONTINUE_BUTTON=(By.CSS_SELECTOR, '.login-button')
    SETTINGS_BUTTON=(By.CSS_SELECTOR, "a[href='/settings']")
    SUBSCRIPTION_AND_PAYMENT_BUTTON=(By.CSS_SELECTOR, "[href='/subscription']")

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')
        sleep(5)

    def login_add(self):
        self.input_text('moussadiak300@gmail.com', *self.EMAIL_TAB)
        self.input_text('Diakite300$', *self.PASSWORD_TAB)
        self.click(*self.CONTINUE_BUTTON)
        sleep(2)

    def click_settings_button(self):
        self.click(*self.SETTINGS_BUTTON)
        sleep(2)


