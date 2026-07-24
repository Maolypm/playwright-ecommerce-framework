from playwright.sync_api import expect
from utils.data_loader import load_test_data

def test_locked_user_login(login_page):

    data = load_test_data()

    login_page.navigate()

    login_page.login(
        data["locked_user"]["username"],
        data["locked_user"]["password"]
    )

    expect(login_page.error_message
           ).to_be_visible()