from Basepage.basepage import BasePage
class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def __init__(self, page):
        super().__init__(page)

    def navigate(self):
        self.open_url("https://www.saucedemo.com")

    def enter_username(self, username):
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login_as(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)