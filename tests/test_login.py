import pytest

@pytest.mark.smoke
@pytest.mark.func
def test_valid_login_standard_user(login_page):
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    assert "inventory" in login_page.page.url, f"Login failed! Expected URL to contain 'inventory', got: {login_page.page.url}"

@pytest.mark.negative
def test_invalid_login_wrong_password(login_page):
    login_page.navigate()
    login_page.login_as("standard_user", "wrong_password")
    error_message = login_page.get_error_message()
    assert error_message is not None, "Error message was not displayed"
    assert "Epic sadface" in error_message, f"Expected 'Epic sadface' in error, got: {error_message}"
    assert "Username and password do not match" in error_message, f"Expected 'do not match' in error, got: {error_message}"

@pytest.mark.negative
def test_locked_out_user(login_page):
    login_page.navigate()
    login_page.login_as("locked_out_user", "secret_sauce")
    error_message = login_page.get_error_message()
    assert error_message is not None, "Error message was not displayed"
    assert "Sorry, this user has been locked out" in error_message, f"Expected lockout message, got: {error_message}"

@pytest.mark.smoke
def test_logout(login_page, inventory_page):
    login_page.navigate()
    login_page.login_as("standard_user", "secret_sauce")
    assert "inventory" in login_page.page.url, "Did not reach inventory page"
    inventory_page.logout()
    assert login_page.is_visible(login_page.LOGIN_BUTTON), "User was not returned to login page"
