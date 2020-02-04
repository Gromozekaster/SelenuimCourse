"""from selenium.webdriver.chrome.options import Options
from selenium import webdriver"""
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    """Поддержка опций."""
    parser.addoption("--language",
                     action="store",
                     default=None,
                     help="Select language")

@pytest.fixture
def browser(request):
    print("\nstart browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()