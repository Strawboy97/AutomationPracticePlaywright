from playwright.sync_api import Page
from pages.login import Login

def test_successful_login(page: Page):
    login_page = Login(page)
    login_page.navigate()
    login_page.login('practice', 'SuperSecretPassword!')

