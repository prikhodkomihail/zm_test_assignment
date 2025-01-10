from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = Options()
        options.add_argument('--blink-settings=imagesEnabled=false')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    width, height = (1920, 1080)
    browser.set_window_size(width, height)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: проверка основной функциональности")