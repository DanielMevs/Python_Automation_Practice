from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormAuthentication(BasePage):
    URL = 'https://the-internet.herokuapp.com'
    AUTH_FORM_LINK = (By.LINK_TEXT, 'Form Authentication')
    USER_NAME = (By.CSS_SELECTOR, '#username')
    PASS_WORD = (By.CSS_SELECTOR, '#password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    LOG_OUT = (By.LINK_TEXT, 'Logout')
    FLASH = (By.CSS_SELECTOR, '#flash')

    def login(self, user_name, pass_word):
        self.driver.get(self.URL)

        self.wait_for(self.AUTH_FORM_LINK).click()

        username = self.wait_for(self.USER_NAME)
        username.send_keys(user_name)

        password = self.find(self.PASS_WORD)

        password.send_keys(pass_word)

        self.find(self.SUBMIT_BUTTON).click()

    def logout(self):
        self.wait_for(self.LOG_OUT).click()
        flash = self.wait_for(self.FLASH)
        assert 'logged out' in flash.text


