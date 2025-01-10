from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(params=[
    ("chrome", (1920, 1080)),
    ("chrome", (1366, 768)),
    ("chrome", (375, 812)),
    ("firefox", (1920, 1080)),
    ("firefox", (1366, 768)),
    ("firefox", (375, 812)),
], ids=[
    "chrome_desktop",
    "chrome_laptop",
    "chrome_mobile",
    "firefox_desktop",
    "firefox_laptop",
    "firefox_mobile"
], scope="function")
def browser(request):
    browser_name, resolution = request.param
    width, height = resolution

    if browser_name == "chrome":
        options = Options()
#        options.add_argument('--blink-settings=imagesEnabled=false')
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    browser.set_window_size(width, height)
    yield browser
    browser.quit()


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: проверка основной функциональности")