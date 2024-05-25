from _pytest.fixtures import fixture

from pages.HomePage import HomePage


def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser')

@fixture()
def browser_selected(request):
    selected_browser = request.config.getoption('--browser_selenium').lower()
    yield selected_browser

@fixture()
def setup(browser_selected):
    # Precondition
    home_page = HomePage(browser=browser_selected)
    home_page.open_home_page()

    # Pos condition
    yield home_page
    home_page.close()
