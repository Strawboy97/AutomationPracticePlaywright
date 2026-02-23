class Secure:
    def __init__(self, page):
        self.page = page
        self.message = page.get_by_text("You logged into a secure area!")
        self.logout_button = page.get_by_role("link", name="Logout")