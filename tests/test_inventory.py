from playwright.sync_api import expect
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
    
    expect(inventory_page.inventory_items_locator()
           ).to_have_count(6)