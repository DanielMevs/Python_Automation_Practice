import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

    yield driver
    driver.quit()
