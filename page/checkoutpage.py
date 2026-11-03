from Basepage.basepage import BasePage

class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    FINISH_BUTTON = "[data-test='finish']"
    CONFIRMATION_HEADER = "[data-test='complete-header']"

    def __init__(self, page):
        super().__init__(page)

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_HEADER)
