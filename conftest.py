import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page, request):
    login_page = LoginPage(page)
    yield login_page

    if (request.node.rep_call.failed):
        page.screenshot(
            path=f"screenshots/{request.node.name}.png"
        )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)