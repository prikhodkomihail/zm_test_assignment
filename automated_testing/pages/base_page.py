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
        self.browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(keyword)
        self.browser.find_element(*BasePageLocators.SEARCH_FIELD).submit()
        # WebDriverWait(self.browser, 10).until(
        #     EC.element_to_be_clickable(BasePageLocators.SEARCH_BTN)
        # )
        # self.browser.find_element(*BasePageLocators.SEARCH_BTN).click()
        # self.browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(keyword + Keys.RETURN)

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except:
            return False
        return True
