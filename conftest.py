import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Language: ru, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
