import pytest
from page.loginpage import LoginPage
from page.inventorypage import InventoryPage
from page.cartpage import CartPage
from page.checkoutpage import CheckoutPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
