import pytest

from pages.secure import Secure
from pages.login import Login

from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    return Login(page)

@pytest.fixture
def secure_page(page: Page):
    return Secure(page)
