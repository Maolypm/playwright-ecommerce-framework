import json
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_loader import load_test_data
from playwright.sync_api import expect

def test_complete_checkout(login_page):

    data = load_test_data()

    with open("data/checkout.json") as file:
        checkout_data = json.load(file)

    login_page.navigate()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    cart_page = CartPage(login_page.page)

    cart_page.add_backpack_to_cart()

    cart_page.open_cart()

    checkout_page = CheckoutPage(login_page.page)

    checkout_page.checkout(
        checkout_data["customer"]["first_name"],
        checkout_data["customer"]["last_name"],
        checkout_data["customer"]["postal_code"]
    )

    expect(checkout_page.confirmation_locator()
           ).to_have_text("Thank you for your order!")