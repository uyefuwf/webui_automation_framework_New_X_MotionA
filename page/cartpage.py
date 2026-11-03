from Basepage.basepage import BasePage

class CartPage(BasePage):
    # Locators
    ITEM_NAME = "[data-test='inventory-item-name']"
    ITEM_QUANTITY = "[data-test='item-quantity']"
    CHECKOUT_BUTTON = "[data-test='checkout']"

    def __init__(self, page):
        super().__init__(page)

    def get_cart_item_names(self):
        return self.get_all_texts(self.ITEM_NAME)

    def get_cart_item_quantities(self):
        return self.get_all_texts(self.ITEM_QUANTITY)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
