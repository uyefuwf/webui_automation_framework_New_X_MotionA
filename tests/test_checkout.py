import pytest

@pytest.mark.smoke
@pytest.mark.func
def test_full_checkout_flow(login_page, inventory_page, cart_page, checkout_page):
    # 6. Complete the full checkout flow: cart -> customer info -> overview -> finish -> confirmation message
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    
    # 1. Add product and open cart
    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()
    assert "cart" in cart_page.page.url, "Not on cart page"
    
    # 2. Click checkout
    cart_page.click_checkout()
    assert "checkout-step-one" in checkout_page.page.url, "Not on checkout step one page"
    
    # 3. Customer info
    checkout_page.fill_customer_info("John", "Doe", "12345")
    checkout_page.click_continue()
    assert "checkout-step-two" in checkout_page.page.url, "Not on checkout overview page"
    
    # 4. Overview -> Finish
    checkout_page.click_finish()
    assert "checkout-complete" in checkout_page.page.url, "Not on checkout complete page"
    
    # 5. Confirmation message
    confirmation_message = checkout_page.get_confirmation_message()
    assert confirmation_message == "Thank you for your order!", f"Unexpected confirmation message: {confirmation_message}"
