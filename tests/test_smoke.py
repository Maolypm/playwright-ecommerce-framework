from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_valid_login(login_page):
    login_page.navigate()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in login_page.page.url