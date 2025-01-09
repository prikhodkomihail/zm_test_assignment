# Тест-кейсы: Локализация поисковой страницы Google

Этот файл содержит тест-кейсы для проверки локализации поисковой страницы Google, включая изменение языка интерфейса и соответствие результатов поиска выбранному языку.

## 1. Изменение языка интерфейса

### TC-051: Изменение языка интерфейса с русского на английский

**ID:** TC-051

**Название:** Изменение языка интерфейса с русского на английский

**Предусловия:** Открыта главная страница Google. Текущий язык интерфейса — русский.

**Шаги:**

1.  Кликнуть на иконку Google Account в правом верхнем углу.
2.  Выбрать раздел "Язык". Убедиться, что произошел переход на страницу "Язык и регион".
3.  Выбрать "Язык интерфейса". В попапе выбора языка отобразится список доступных языков.
4.  В поиске ввести "English". Кликнуть на строку "English (английский)". Убедиться, что возле строки "English (английский)" отобразилась галочка.
5.  Кликнуть на кнопку "Подтвердить".
6.  Перейти на главную страницу Google.

**Ожидаемый результат:**

*   Интерфейс Google (текст на кнопках, ссылки, сообщения и т.д.) отображается на английском языке.

### TC-052: Проверка сохранения английского языка после перезагрузки страницы

**ID:** TC-052

**Название:** Проверка сохранения английского языка после перезагрузки страницы

**Предусловия:** Открыта главная страница Google. Язык интерфейса установлен на английский.

**Шаги:**

1.  Перезагрузить страницу Google.

**Ожидаемый результат:**

*   Язык интерфейса остается установленным на английский.

### TC-053: Проверка возврата на русский язык

**ID:** TC-053

**Название:** Проверка возврата на русский язык

**Предусловия:** Открыта главная страница Google. Язык интерфейса установлен на английский.

**Шаги:**

1.  Кликнуть на иконку Google Account в правом верхнем углу.
2.  Выбрать раздел "Language". Убедиться, что произошел переход на страницу "Language and region".
3.  Выбрать "Display language". В попапе выбора языка отобразится список доступных языков.
4.  В поиске ввести "русский". Кликнуть на строку "русский (Russian)". Убедиться, что возле строки "русский (Russian)" отобразилась галочка.
5.  Кликнуть на кнопку "Confirm".
6.  Перейти на главную страницу Google.

**Ожидаемый результат:**

*   Интерфейс Google отображается на русском языке.

## 2. Соответствие результатов поиска английскому языку

### TC-054: Поиск на английском языке с английским интерфейсом

**ID:** TC-054

**Название:** Поиск на английском языке с английским интерфейсом

**Предусловия:** Открыта главная страница Google. Язык интерфейса установлен на английский.

**Шаги:**

1.  Ввести поисковый запрос на английском языке (например, "programming").
2.  Нажать Enter.

**Ожидаемый результат:**

*   Результаты поиска преимущественно на английском языке.
*   Интерфейс страницы результатов поиска (пагинация, фильтры и т.д.) на английском языке.

### TC-055: Поиск на русском языке с английским интерфейсом

**ID:** TC-055

**Название:** Поиск на русском языке с английским интерфейсом

**Предусловия:** Открыта главная страница Google. Язык интерфейса установлен на английский.

**Шаги:**

1.  Ввести поисковый запрос "программирование" на русском языке.
2.  Нажать Enter.

**Ожидаемый результат:**

*   Результаты поиска преимущественно на русском языке.
*   Интерфейс страницы результатов поиска на английском языке.

## 3. Негативные тесты

### TC-056: Отображение смешанного текста (частично на русском, частично на английском)

**ID:** TC-056

**Название:** Отображение смешанного текста

**Предусловия:** Открыта главная страница Google. Язык интерфейса установлен на английский.

**Шаги:**

1.  Ввести поисковый запрос, содержащий слова на разных языках (например, "программирование software").

**Ожидаемый результат:**

*   Результаты поиска преимущественно на русском языке.
*   Интерфейс страницы результатов поиска на английском языке.