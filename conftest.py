import pytest
from page.loginpage import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

