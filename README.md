# Тестирование поиска Google

Данный проект содержит результаты тестирования функциональности поиска на сайте google.com.

## Описание

В рамках тестового задания было проведено ручное и автоматизированное тестирование основных функций поиска, включая расширенный поиск, визуальное тестирование и тестирование локализации.

## Инструменты

*   **Язык программирования:** Python
*   **Фреймворк для автоматизации:** Selenium
*   **Браузер:** Chrome, Firefox
*   **Плагин для параллельного запуска:** pytest-xdist 3.3.1
*   **Генерация HTML отчетов:** pytest-html 3.1.1

## Ручное тестирование

Тест-кейсы для проведения ручного тестирования доступны в папке [manual_testing](./manual_testing).

## Запуск тестов

Для запуска автоматизированных тестов необходимо:

1.  Установить зависимости: `pip install -r requirements.txt`
2.  Запустить тесты: `pytest -v --tb=line -m smoke`
3.  Для запуска тестов с фильтрацией: `pytest -v --tb=line -m smoke -k "<параметр фильтрации>, например chrome"`
4.  Для запуска нескольких тестов параллельно: `pytest -v --tb=line -m smoke -n auto`
5.  Для запуска с генерацией отчета: `pytest --html=reports/report.html --self-contained-html`
  
## Результаты

[Отчет по автоматизации тестирования](./reports/report.html) доступен для просмотра.

## Важный комментарий
Если тесты в Chrome не проходят из-за "бесконечной загрузки", то необходимо расскоментировать строку 28 с параметром
`options.add_argument('--blink-settings=imagesEnabled=false')` в файле [conftest.py](./automated_testing/conftest.py)

## Возможные направления для улучшения проекта

* **Добавление чеклистов**: создание структурированных списков проверок для ручного тестирования.  
* **Тестирование фильтров результатов поиска**: проверка корректности работы фильтров (например, по дате или типу контента).  
* **Отчет по ручному тестированию**: систематизация и документирование результатов ручных проверок.  
* **Автоматизация негативных тестов**: внедрение тестов, проверяющих корректность обработки некорректных данных и ошибок.  
* **Расширение поддержки браузеров**: добавление возможности запуска тестов в Safari и других популярных браузерах.  
* **Рефакторинг текущего кода**: оптимизация существующих тестов, устранение дублирования кода и внедрение новых проверок.