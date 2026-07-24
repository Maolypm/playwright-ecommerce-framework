from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.data_loader import load_test_data

def test_valid_login(login_page):

    test_data = load_test_data()

    login_page.navigate()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    expect(login_page.page).to_have_url(
        "https://www.saucedemo.com/inventory.html")