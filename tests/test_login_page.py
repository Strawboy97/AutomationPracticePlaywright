import re

from playwright.sync_api import Page, expect
from pages.login import Login
from pages.secure import Secure

def test_successful_login(page: Page):
    login_page = Login(page)
    secure_page = Secure(page)

    login_page.navigate()
    login_page.login('practice', 'SuperSecretPassword!')
    expect(page).to_have_url(re.compile("secure$"))
    expect(secure_page.message).to_be_visible()
    expect(secure_page.logout_button).to_be_visible()