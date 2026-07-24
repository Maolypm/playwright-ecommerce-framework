from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_badge = ".shopping_cart_badge"

    def add_backpack_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")

    def get_cart_count(self):
        return self.page.locator(
            self.cart_badge
        ).inner_text()

    def open_cart(self):
        self.page.click(".shopping_cart_link")

    def cart_badge_locator(self):
        return self.page.locator(self.cart_badge)