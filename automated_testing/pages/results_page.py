from ..pages.base_page import BasePage
from ..pages.locators import SearchResultsPageLocators
import re
from bs4 import BeautifulSoup
import unicodedata
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(BasePage):
    def check_results_exist(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        results = self.browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
        assert results, "Результаты поиска не отображаются"

    def check_browser_title(self, keyword):
        assert keyword in self.browser.title, \
            f"Название страницы {self.browser.title} не соответствует ключевому слову '{keyword}'"

    def clean_text(self, text):
        if text is None:
            return ""
        soup = BeautifulSoup(text, "html.parser") if text else None
        clean_text = soup.get_text() if soup else text  # Обрабатываем None
        clean_text = clean_text.replace("\xa0", " ")
        clean_text = re.sub(r'\s+', ' ', clean_text)
        clean_text = unicodedata.normalize('NFKD', clean_text)
        clean_text = "".join([c for c in clean_text if unicodedata.category(c) != 'Mn'])  # Удаляем знаки модификации
        clean_text = clean_text.strip().lower()
        return clean_text

    def check_exact_keyword_in_results(self, keyword):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        results = self.browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
        result_text = [result.text.lower() for result in results if result.text.strip()]

        for result in result_text[:5]:
            assert keyword.lower() in result, \
                f"Точное совпадение ключевого слова '{keyword}' не найдено в выдаче ссылок: {result_text[:5]}"

    def check_keyword_in_results(self, keyword):
        # Составляем регулярное выражение
        # \b - границы слова, чтобы избежать совпадений внутри других слов
        pattern = rf"\b{re.escape(keyword.lower()[:-2])}[а-яё]*\b"  # Убираем последние 2 буквы, добавляем любую последовательность букв

        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        results = self.browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
        result_text = [result.text.lower() for result in results if result.text.strip()]

        for result in result_text[:5]:
            assert re.search(pattern, result), f"Ключевое слово '{keyword}' не найдено в выдаче ссылок: {result_text[:5]}"

    def check_exact_snippets_in_results(self, keyword):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        results = self.browser.find_elements(*SearchResultsPageLocators.SNIPPETS)
        result_text = [self.clean_text(result.text.lower()) for result in results if result.text.strip()]

        for result in result_text[:5]:
            assert keyword.lower() in result, \
                f"Точное совпадение ключевого слова '{keyword}' не найдено в сниппетах: {result_text[:5]}"

    def check_snippets_in_results(self, keyword):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        pattern = rf"\b{re.escape(keyword.lower()[:-2])}[а-яё]*\b"

        results = self.browser.find_elements(*SearchResultsPageLocators.SNIPPETS)
        result_text = [self.clean_text(result.text.lower()) for result in results if result.text.strip()]

        for result in result_text[:5]:
            assert re.search(pattern, result), f"Ключевое слово '{keyword}' не найдено в сниппетах: {result_text[:5]}"

    def check_results_for_keyword_exclusion(self, exclude_keyword):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(SearchResultsPageLocators.RESULT_LINKS)
        )

        results = self.browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
        result_text = [result.text.lower() for result in results if result.text.strip()]
        for result in result_text[:5]:
            assert exclude_keyword.lower() not in result, \
                f"Исключенное слово '{exclude_keyword}' найдено в выдаче ссылок: {result_text[:5]}"

        snippets = self.browser.find_elements(*SearchResultsPageLocators.SNIPPETS)
        snippets_text = [self.clean_text(snippet.text.lower()) for snippet in snippets if snippet.text.strip()]
        for snippet in snippets_text[:5]:
            assert exclude_keyword.lower() not in snippet, \
                f"Исключенное слово '{exclude_keyword}' найдено в выдаче сниппетов: {snippets_text[:5]}"
