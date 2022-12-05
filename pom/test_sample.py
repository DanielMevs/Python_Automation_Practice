import pytest
from pages.home import Home
from pages.form_authentication import FormAuthentication
from confest import driver
@pytest.mark.usefixtures("driver")
def test_form_authentication_login_logout(driver):
    home_page = Home()
    form_auth = home_page.go_to_login(driver=driver)
    form_auth.login()
    form_auth.logout()

