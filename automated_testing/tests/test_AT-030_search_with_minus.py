from ..pages.results_page import SearchResultsPage
from ..pages.base_page import BasePage
import pytest


@pytest.mark.smoke
def test_search_with_quotes(browser):
    link = "https://www.google.com/"
    include_keyword = "программирование"
    exclude_keyword = "Java"
    keyword = f'{include_keyword} -{exclude_keyword}'

    base_page = BasePage(browser, link)
    base_page.open()
    base_page.search(keyword)

    search_page = SearchResultsPage(browser, browser.current_url)
    search_page.check_results_exist()
    search_page.check_browser_title(keyword)
    search_page.check_keyword_in_results(include_keyword)
    search_page.check_snippets_in_results(include_keyword)
    search_page.check_results_for_keyword_exclusion(exclude_keyword)
