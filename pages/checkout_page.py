from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def checkout(self, first_name, last_name, postal_code):

        self.page.click("#checkout")

        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)

        self.page.click("#continue")

        self.page.click("#finish")

    def get_confirmation_text(self):
        return self.page.locator(".complete-header").inner_text()

    def confirmation_locator(self):
        return self.page.locator(".complete-header")