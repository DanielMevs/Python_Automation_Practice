from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormAuthentication(object):
    URL = 'https://the-internet.herokuapp.com'
    AUTH_FORM_LINK = (By.LINK_TEXT, 'Form Authentication')
    USER_NAME = (By.CSS_SELECTOR, '#username')
    PASS_WORD = (By.CSS_SELECTOR, '#password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type=submit]')
    LOG_OUT = (By.LINK_TEXT, 'Logout')
    FLASH = (By.CSS_SELECTOR, '#flash')

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, user_name, pass_word):
        self.driver.get(self.URL)

        self.wait.until(EC.presence_of_element_located(self.AUTH_FORM_LINK)).click()

        username = self.wait.until(EC.presence_of_element_located(self.USER_NAME))
        username.send_keys(user_name)

        password = self.driver.find_element(*self.PASS_WORD)

        password.send_keys(pass_word)

        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def logout(self):
        self.wait.until(EC.presence_of_element_located(self.LOG_OUT)).click()
        flash = self.wait.until(EC.presence_of_element_located(self.FLASH))
        assert 'logged out' in flash.text


