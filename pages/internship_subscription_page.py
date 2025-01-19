from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class InternshipSubscriptionPage(BasePage):
    HEADER= (By.CSS_SELECTOR, "[class='lotion-your-h3--price size']")
    UPGRADE_PLAN_BUTTON=(By.CSS_SELECTOR, "[wized='upgradePlanButton']")
    BACK_BUTTON=(By.CSS_SELECTOR, ".button-verify[href='/settings']")

    def verify_page(self):
        self.verify_partial_url('subscription')

    def verify_header(self):
        self.find_element(*self.HEADER)

    def verify_back_and_upgrade_plan_buttons(self):
        self.find_element(*self.UPGRADE_PLAN_BUTTON)
        self.find_element(*self.BACK_BUTTON)