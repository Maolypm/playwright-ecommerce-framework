from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.inventory_items = ".inventory_item"

    def get_products_count(self):
        return self.page.locator(
            self.inventory_items
        ).count()