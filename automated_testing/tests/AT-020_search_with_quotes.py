from ..pages.results_page import SearchResultsPage
from ..pages.base_page import BasePage
import pytest


@pytest.mark.smoke
def test_search_with_quotes(browser):
    link = "https://www.google.com/"
    keyword = "портрет Дориана Грея"

    base_page = BasePage(browser, link)
    base_page.open()
    base_page.search(f'"{keyword}"')

    search_page = SearchResultsPage(browser, browser.current_url)
    search_page.check_results_exist()
    search_page.check_browser_title(keyword)
    search_page.check_exact_keyword_in_results(keyword)
    search_page.check_exact_snippets_in_results(keyword)

