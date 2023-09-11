import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Available values: Chrome, Firefox"
    )

@pytest.fixture(scope="session")
def browser(request):
    driver:str = request.config.getoption("--browser")
    if driver.lower() == "chrome":
        browser = webdriver.Chrome()
    elif driver.lower() == "firefox":
        browser = webdriver.Firefox()
    else:
        browser = webdriver.Chrome()
    yield browser
    browser.quit()
        

