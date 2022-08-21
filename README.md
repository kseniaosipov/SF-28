# SF-28
 Финальное задание по изучению автоматизации тестирования

Из предложенных в задании выбран сайт интернет-магазина Лабиринт - https://www.labirint.ru/ 

 Запуск тестов:

1) Установить все внешние зависимости командой   
```pip install -r requirements.txt```

2) Скачать версию Selenium WebDriver, совместимую с вашим браузером  
(тесты проводились в браузере Google Chrome на операционной системе MacOC)

3) Запуск тестов командами:

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_main_page_header.py```

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_main_page_body.py```

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_main_page_footer.py```

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_search.py```

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_book_page.py```

```python -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} tests/test_card_page.py```

   где ${PATH_TO_DRIVER} находится путь к драйверу Selenium для текущей ОС

Тесты в папке tests. 
test_book_page.py - содержит тесты на ссылки на странице открытой книги
test_card_page.py - тесты на работоспособность корзины
test_main_page_body.py - проверка ссылок и кнопок в теле главной страницы
test_main_page_footer.py - проверка ссылок и кнопок в footer главной страницы
test_main_page_header.py - проверка ссылок и кнопок в header главной страницы
test_search.py - проверка поиска
