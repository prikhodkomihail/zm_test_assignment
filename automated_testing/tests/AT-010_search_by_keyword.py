from ..pages.locators import BasePageLocators
from ..pages.results_page import SearchResultsPage


def test_search_by_keyword(browser):
    browser.get("https://www.google.com/")
    keyword = "тестирование"
    browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(keyword)
    browser.find_element(*BasePageLocators.SEARCH_BTN).click()

    search_page = SearchResultsPage(browser, browser.current_url)
    search_page.check_results_exist()
    search_page.check_browser_title(keyword)
