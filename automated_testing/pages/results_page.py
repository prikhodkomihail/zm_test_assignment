from automated_testing.pages.base_page import BasePage
from automated_testing.pages.locators import SearchResultsPageLocators

# class SearchResultsPage(BasePage):
#     def check_results_exist(self):
#         results = browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
#         assert len(results) > 0, "Результаты поиска не отображаются"