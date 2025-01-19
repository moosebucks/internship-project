from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class InternshipSettingsPage(BasePage):
    SUBSCRIPTION_AND_PAYMENT_BUTTON = (By.CSS_SELECTOR, "[href='/subscription']")

    def click_subscription_and_payments(self):
        self.click(*self.SUBSCRIPTION_AND_PAYMENT_BUTTON)
        sleep(2)