import re

from playwright.sync_api import Page, expect
from pages.login import Login
from pages.secure import Secure

def test_successful_login(page: Page):
    login_page = Login(page)
    secure_page = Secure(page)

    # Navigate to Login Page
    login_page.navigate()

    #Verify that the login page is displayed successfully.
    expect(login_page.breadcrumb).to_be_visible()

    # Login with Correct credentials
    login_page.login('practice', 'SuperSecretPassword!')

    # Verify that the user is redirected to the /secure page.
    expect(page).to_have_url(re.compile("secure$"))

    # Confirm the success message "You logged into a secure area!" is visible.
    expect(secure_page.message).to_be_visible()

    #Verify that a Logout button is displayed.
    expect(secure_page.logout_button).to_be_visible()