import pytest
from selenium import webdriver

def pytest_adoption(parser):
    parser.adoption("--url", action="store", help="the url for our site", default="https://the-internet.herokuapp.com")
    parser.adoption("--username", action="store", help="the username for our account", default="tomsmith")
    parser.adoption("--password", action="store", help="the password for our account", default="SuperSecretPassword!")


def pytest_generate_tests(metafunc):
    url = metafunc.config.option.url
    username = metafunc.config.option.username
    password = metafunc.config.option.password

    if 'url' in metafunc.fixturenames and url is not None and \
            'username' in metafunc.fixturenames and username is not \
            None and 'password' in metafunc.fixturenames and password is not None:
        metafunc.parameterize('url', [url])
        metafunc.parameterize('username', [username])
        metafunc.parameterize('password')



@pytest.fixture()
def driver(pytestconfig):
    url = pytestconfig.getoption("url")
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver.get(url)

    yield driver
    driver.quit()
