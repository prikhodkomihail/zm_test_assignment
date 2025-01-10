from selenium.webdriver.common.by import By


class BasePageLocators():
    SEARCH_FIELD = (By.NAME, 'q')
    SEARCH_BTN = (By.NAME, 'btnK')


class SearchResultsPageLocators():
    RESULT_LINKS = (By.CSS_SELECTOR, 'h3')
    SNIPPETS = (By.CSS_SELECTOR, '[data-sncf="1"] em')
