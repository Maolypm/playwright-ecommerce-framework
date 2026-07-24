from pages.inventory_page import InventoryPage
from utils.data_loader import load_test_data

def test_inventory_products_count(login_page):

    data = load_test_data()

    login_page.navigate()

    login_page.login(
        data["valid_user"]["username"],
        data["valid_user"]["password"]
    )

    inventory_page = InventoryPage(
        login_page.page)
    
    assert inventory_page.get_products_count() == 6