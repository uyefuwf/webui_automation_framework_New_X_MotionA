from Basepage.basepage import BasePage

class InventoryPage(BasePage):
    # Locators
    ADD_TO_CART_BACKPACK = "[data-test='add-to-cart-sauce-labs-backpack']"
    ADD_TO_CART_BIKE_LIGHT = "[data-test='add-to-cart-sauce-labs-bike-light']"
    CART_BADGE = "[data-test='shopping-cart-badge']"
    CART_LINK = "[data-test='shopping-cart-link']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    ITEM_PRICES = "[data-test='inventory-item-price']"
    BURGER_MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "[data-test='logout-sidebar-link']"

    def __init__(self, page):
        super().__init__(page)

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def add_bike_light_to_cart(self):
        self.click(self.ADD_TO_CART_BIKE_LIGHT)

    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)

    def select_sort_option(self, option_value):
        self.select_option(self.SORT_DROPDOWN, option_value)

    def get_item_prices(self):
        prices_text = self.get_all_texts(self.ITEM_PRICES)
        return [float(p.replace("$", "")) for p in prices_text]

    def logout(self):
        self.click(self.BURGER_MENU_BUTTON)
        self.wait_for_visible(self.LOGOUT_LINK)
        self.click(self.LOGOUT_LINK)
