from ..pages.results_page import SearchResultsPage
from ..pages.base_page import BasePage
import pytest
from ..pages.locators import SearchResultsPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.smoke
def test_search_by_keyword(browser):
    link = "https://www.google.com/"
    keyword = "тестирование"

    base_page = BasePage(browser, link)
    base_page.open()
    base_page.search(keyword)

    search_page = SearchResultsPage(browser, browser.current_url)
    search_page.check_results_exist()
    search_page.check_browser_title(keyword)
    search_page.check_keyword_in_results(keyword)
    search_page.check_snippets_in_results(keyword)


