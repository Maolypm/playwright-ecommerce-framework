from pages.cart_page import CartPage
from utils.data_loader import load_test_data

def test_add_product_to_cart(login_page):

    data = load_test_data()

    login_page.navigate()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    cart_page = CartPage(login_page.page)

    cart_page.add_backpack_to_cart()

    assert cart_page.get_cart_count() == "1"