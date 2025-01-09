# Тест-кейсы: Поиск с использованием минус-оператора

Этот файл содержит тест-кейсы для проверки функциональности поиска с использованием минус-оператора в Google. Минус-оператор используется для исключения определенных слов из результатов поиска.

## Позитивные тесты

### TC-031: Исключение одного слова из поиска

**ID:** TC-031

**Название:** Поиск "программирование -java"

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "программирование -java".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Отображаются результаты поиска, содержащие слово "программирование", но *не* содержащие слово "java".
*   Результаты, содержащие оба слова ("программирование" и "java"), отсутствуют или находятся значительно ниже в списке результатов.

### TC-032: Исключение нескольких слов из поиска

**ID:** TC-032

**Название:** Поиск "разработка -веб -мобильных"

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "разработка -веб -мобильных".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Отображаются результаты поиска, содержащие слово "разработка", но *не* содержащие ни "веб", ни "мобильных".
*   Результаты, содержащие любое из исключенных слов ("веб" или "мобильных"), отсутствуют или находятся значительно ниже в списке.

### TC-033: Исключение слова с разным регистром

**ID:** TC-033

**Название:** Поиск "ТеСтИрОвАнИе -JAvA"

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "ТеСтИрОвАнИе -JAvA".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Результаты поиска идентичны результатам поиска по запросу "тестирование -java" (в нижнем регистре). Регистр исключаемого слова не влияет на результат.

## Негативные тесты

### TC-034: Исключение с пробелами перед минусом

**ID:** TC-034

**Название:** Поиск "тестирование   -java" (с пробелами перед минусом)

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "тестирование   -java".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Система обрабатывает запрос.
*   Результаты поиска идентичны результатам поиска "тестирование -java" (без лишних пробелов).

### TC-035: Исключение с пробелами после минуса

**ID:** TC-035

**Название:** Поиск "тестирование -   java" (с пробелами после минуса)

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "тестирование -   java".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Система обрабатывает запрос.
*   Результаты поиска идентичны результатам поиска "тестирование -java" (без лишних пробелов).

### TC-036: Исключение с несколькими минусами подряд

**ID:** TC-036

**Название:** Поиск "тестирование --java"

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1.  Ввести в поисковую строку "тестирование --java".
2.  Нажать Enter.

**Ожидаемый результат:**

*   Система обрабатывает запрос.
*   Результаты поиска идентичны результатам поиска "тестирование -java" (один минус).

### TC-037: Исключение фразы в кавычках

**ID:** TC-037

**Название:** Поиск "разработка -"мобильная разработка""

**Предусловия:** Открыта главная страница Google.

**Шаги:**

1. Ввести в поисковую строку "разработка -"мобильная разработка"".
2. Нажать Enter.

**Ожидаемый результат:**

* Система обрабатывает запрос.
* Кавычки игнорируются. Результаты поиска идентичны результатам поиска "разработка -мобильная разработка".