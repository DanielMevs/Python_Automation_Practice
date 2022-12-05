from selenium.webdriver.common.by import By
from .base_page import BasePage
from form_authentication import FormAuthentication

class Home(BasePage):

    AUTH_FORM_LINK = (By.LINK_TEXT, 'Form Authentication')

    def go_to_login(self, driver):
        self.wait_for(self.AUTH_FORM_LINK).click()
        return FormAuthentication(driver)