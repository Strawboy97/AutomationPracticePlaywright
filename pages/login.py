class Login:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.breadcrumb = page.get_by_text("Login Page", exact=True)
        self.alert = page.get_by_role("alert")

    def navigate(self):
        self.page.goto("https://practice.expandtesting.com/login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()