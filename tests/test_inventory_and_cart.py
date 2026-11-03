import pytest

@pytest.mark.smoke
def test_add_single_product_to_cart_badge_count(login_page, inventory_page):
    # 4. Add a single product to the cart and verify the cart badge count
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    badge_count = inventory_page.get_cart_badge_count()
    assert badge_count == "1", f"Expected cart badge count '1', got: {badge_count}"

@pytest.mark.func
def test_add_multiple_products_and_verify_cart(login_page, inventory_page, cart_page):
    # 5. Add multiple products, open the cart, and verify items and quantities
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.open_cart()
    
    items = cart_page.get_cart_item_names()
    quantities = cart_page.get_cart_item_quantities()
    
    assert "Sauce Labs Backpack" in items, "Sauce Labs Backpack not found in cart"
    assert "Sauce Labs Bike Light" in items, "Sauce Labs Bike Light not found in cart"
    assert quantities == ["1", "1"], f"Expected quantities ['1', '1'], got: {quantities}"

@pytest.mark.func
def test_sort_products_price_low_to_high(login_page, inventory_page):
    # 7. Sort products (Price low to high) and assert the ordering is correct
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    
    inventory_page.select_sort_option("lohi")
    prices = inventory_page.get_item_prices()
    
    assert len(prices) > 0, "No product prices found"
    assert prices == sorted(prices), f"Prices are not sorted low to high: {prices}"
