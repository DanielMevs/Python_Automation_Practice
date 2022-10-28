import pytest

from pages.form_authentication import FormAuthentication
from confest import driver

@pytest.mark.usefixtures("driver")
def test_form_authentication_login_logout(driver):
    form_auth = FormAuthentication(driver=driver )
    form_auth.login(user_name='tomsmith', pass_word='SuperSecretPassword!')
    form_auth.logout()

