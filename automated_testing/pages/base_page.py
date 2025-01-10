from ..pages.locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def search(self, keyword):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(BasePageLocators.SEARCH_FIELD)
        )
        self.browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(keyword)
        self.browser.find_element(*BasePageLocators.SEARCH_FIELD).submit()

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except:
            return False
        return True
