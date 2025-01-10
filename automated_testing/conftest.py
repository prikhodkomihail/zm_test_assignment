from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security')
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(10)
    yield browser
    browser.quit()
