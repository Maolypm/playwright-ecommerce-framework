from playwright.sync_api import Page

def test_homepage(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"