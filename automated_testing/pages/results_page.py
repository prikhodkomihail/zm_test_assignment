from ..pages.base_page import BasePage
from ..pages.locators import SearchResultsPageLocators
import re
from bs4 import BeautifulSoup
import unicodedata


class SearchResultsPage(BasePage):
    def check_results_exist(self):
        assert self.is_element_present(*SearchResultsPageLocators.RESULT_LINKS), "Результаты поиска не отображаются"

    def check_browser_title(self, keyword):
        assert keyword in self.browser.title, \
            f"Название страницы {self.browser.title} не соответствует ключевому слову '{keyword}'"

    def clean_text(self, text):
        # Убираем все HTML-теги
        soup = BeautifulSoup(text, "html.parser")
        clean_text = soup.get_text()

        # Заменяем неразрывные пробелы на обычные
        clean_text = clean_text.replace("\xa0", " ")

        # Заменяем множественные пробелы на один
        clean_text = re.sub(r'\s+', ' ', clean_text)

        # Убираем акценты (нормализация)
        # Только удаляем акценты, если это необходимо для корректного поиска
        clean_text = unicodedata.normalize('NFKD', clean_text).encode('ASCII', 'ignore').decode('ASCII')

        # Убираем ведущие и завершающие пробелы
        clean_text = clean_text.strip()

        return clean_text.lower()

    def check_keyword_in_results(self, keyword):
        # Составляем регулярное выражение
        # \b - границы слова, чтобы избежать совпадений внутри других слов
        pattern = rf"\b{re.escape(keyword[:-2])}[а-яё]*\b"  # Убираем последние 2 буквы, добавляем любую последовательность букв

        results = self.browser.find_elements(*SearchResultsPageLocators.RESULT_LINKS)
        result_text = [result.text.lower() for result in results if result.text.strip()]

        # Отладочный вывод
        for result in result_text[:5]:
            print(result)

        for result in result_text[:5]:
            assert re.search(pattern, result), f"Ключевое слово '{keyword}' не найдено в результате: {result_text}"

    def check_snippets_in_results(self, keyword):
        results = self.browser.find_elements(*SearchResultsPageLocators.SNIPPETS)
        result_text = [self.clean_text(result.get_attribute('innerHTML')) for result in results]

        # Отладочный вывод
        for result in result_text[:5]:
            print(result)

        for result in result_text[:5]:
            assert keyword.lower() in result, f"Ключевое слово '{keyword}' не найдено в сниппетах: {result_text}"
