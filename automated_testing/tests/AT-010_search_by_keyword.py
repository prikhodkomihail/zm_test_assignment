from automated_testing.pages.locators import BasePageLocators
from selenium.webdriver.common.by import By


def test_search_by_keyword(browser):
    browser.get("https://www.google.com/")
    keyword = "тестирование"
    browser.find_element(*BasePageLocators.SEARCH_FIELD).send_keys(keyword)
    browser.find_element(*BasePageLocators.SEARCH_BTN).click()
    assert "тестирование" in browser.title

    results = browser.find_elements(By.CSS_SELECTOR, "div.g")
    assert len(results) > 0, "Результаты поиска не отображаются"

    for result in results[:5]:
        result_text = result.text.lower()
        assert keyword.lower() in result_text, f"Ключевое слово '{keyword}' не найдено в результате: {result_text}"
