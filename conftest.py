import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions

from data.constants import LANGUAGES


def pytest_addoption(parser: pytest.Parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help=f'Choose language. Available languages: {LANGUAGES}')


@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> [webdriver.Chrome, webdriver.Firefox]:
    """Select browser and"""
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FFOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def browser_name(request: pytest.FixtureRequest):
    return request.config.getoption('browser_name')


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "language" in metafunc.fixturenames:
        language = metafunc.config.getoption("language")
        metafunc.parametrize("language", [language])
    if "browser" in metafunc.fixturenames:
        browser = metafunc.config.getoption("browser_name")
        metafunc.parametrize('browser_name', [browser])
