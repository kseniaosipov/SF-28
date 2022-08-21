import pytest
from pages.search import Search


# 1 проверка простого поискового запроса
def test_check_simple_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # выведеные первые 60 рузультатов:
    assert page.products_titles.count() == 60, 'Не выведены первые 60 результатов'
    # результаты корректные:
    for title in page.products_titles.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'истори' in title.lower(), msg


# 2 проверка сложного поискового запроса
def test_check_hard_search(web_browser):
    page = Search(web_browser)
    page.search = 'история искусств'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты корректные:
    for title in page.products_titles.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'история искусств' or 'истории искусств' in title.lower(), msg


# 3 проверка автозамены поискового запроса при ошибочной английской раскладке
def test_check_eng_error_search(web_browser):
    page = Search(web_browser)
    page.search = 'bcnjhb'    # истори
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_titles.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'истори' in title.lower(), msg


# 4 проверка автозамены поискового запроса при орфографической ошибке
def test_check_spelling_error_search(web_browser):
    page = Search(web_browser)
    page.search = 'малако'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты автозамены корректные:
    title = page.page_title.get_text()
    msg = 'Неверный результат автозамены "{}"'.format(title)
    assert title == 'Все, что мы нашли в Лабиринте по запросу «молоко»', msg
    # результаты поиска корректные:
    for title in page.products_titles.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'молоко' in title.lower(), msg


# 5 проверка поиска при вводе цифр
def test_check_numbers_search(web_browser):
    page = Search(web_browser)
    page.search = '1941'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_titles.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert '1941' in title, msg


# 6 проверка поиска при вводе символов
def test_check_symbols_search(web_browser):
    page = Search(web_browser)
    page.search = '*/@%!+'
    page.search_run_button.click()
    # не найдено ни одного результата:
    assert page.products_titles.count() == 0
    # корректная информация о результате:
    assert page.msg_search_er.get_text() == "Мы ничего не нашли по вашему запросу! Что делать?"


# 7 проверка поиска по электронным книгам
def test_check_electronic_books_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем Бумажные книги:
    page.without_paper_books_button.click()
    # убираем Прочие товары:
    page.without_others_products_button.click()
    # найдено не менее одного результата:
    assert page.products_titles_electronic.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


# 8 проверка поиска по бумажным книгам
def test_check_paper_books_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем Электронные книги:
    page.without_electronic_books_button.click()
    # убираем Прочие товары:
    page.without_others_products_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert ('электронная' not in title.lower()) and \
               ('CD' not in title.lower()) and \
               ('DVD' not in title.lower()), msg


# 9 проверка поиска по Прочие товары
def test_check_other_goods_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем Бумажные книги:
    page.without_paper_books_button.click()
    # убираем Электронные книги:
    page.without_electronic_books_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'


# 10 проверка поиска по фильтру-кнопке В наличии
def test_check_in_stock_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем Предзаказ:
    page.sort_products_by_type_order.click()
    # убираем Ожидаются:
    page.sort_products_by_type_waiting.click()
    # убираем Нет в продаже:
    page.sort_products_by_type_out_of_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_in_stock.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'корзин' in title.lower(), msg


# 11 проверка поиска по фильтру-кнопке Предзаказ
def test_check_preorder_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем В наличии:
    page.sort_products_by_type_in_stock_is.click()
    # убираем Ожидаются:
    page.sort_products_by_type_waiting.click()
    # убираем Нет в продаже:
    page.sort_products_by_type_out_of_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_waiting.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'предзаказ' in title.lower(), msg


# 12 проверка поиска по фильтру-кнопке Ожидается
def test_check_expected_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # убираем В наличии:
    page.sort_products_by_type_in_stock_is.click()
    # убираем Предзаказ:
    page.sort_products_by_type_order.click()
    # убираем Нет в продаже:
    page.sort_products_by_type_out_of_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_waiting.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'ожидается' in title.lower(), msg


# 13 проверка поиска по фильтру-кнопке Нет в продаже
def test_check_not_on_sale_search(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # скроллим меню с прокруткой
    page.scroll_menu.scroll_to_element()
    # убираем В наличии:
    page.sort_products_by_type_in_stock_is.click()
    # убираем Предзаказ:
    page.sort_products_by_type_order.click()
    # убираем Ожидаются:
    page.sort_products_by_type_waiting.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_waiting.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'нет в продаже' in title.lower(), msg


# 14 проверка поиска по фильтру-списку ТИП ТОВАРА --> Электронные книги
def test_check_electronic_books_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем ТИП ТОВАРА:
    page.product_type.click()
    # нажимаем Бумажные книги:
    page.paper_books.click()
    # нажимаем Другие товары:
    page.other_goods.click()
    # нажимаем на Показать:
    page.show_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types_electronic.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'электронная' in title.lower(), msg


# 15 проверка поиска по фильтру-списку ТИП ТОВАРА --> Бумажные книги
def test_check_paper_books_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем на ТИП ТОВАРА:
    page.product_type.click()
    # нажимаем Электронные книги:
    page.electronic_books.click()
    # нажимаем Другие товары:
    page.other_goods.click()
    # нажимаем Показать:
    page.show_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert ('электронная' not in title.lower()) and \
               ('CD' not in title.lower()) and \
               ('DVD' not in title.lower()), msg


# 16 проверка поиска по фильтру-списку ТИП ТОВАРА --> Другие товары
def test_check_other_goods_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем ТИП ТОВАРА:
    page.product_type.click()
    # нажимаем Бумажные книги:
    page.paper_books.click()
    # нажимаем Электронные книги:
    page.electronic_books.click()
    # нажимаем Показать:
    page.show_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert ('электронная' not in title.lower()) or \
               ('CD' in title.lower()) or \
               ('DVD' in title.lower()), msg


# 17 проверка поиска по фильтру-списку НАЛИЧИЕ --> В наличии
def test_check_in_stock_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем НАЛИЧИЕ:
    page.product_stock.click()
    # нажимаем Предзаказ:
    page.pre_order.click()
    # нажимаем Ожидаются:
    page.waiting.click()
    # нажимаем Нет в продаже:
    page.out_of_stock.click()
    # нажимаем на Показать:
    page.show_button_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types_basket.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'корзин' in title.lower(), msg


# 18 проверка поиска по фильтру-списку НАЛИЧИЕ --> Предзаказ
def test_check_pre_order_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем на НАЛИЧИЕ:
    page.product_stock.click()
    # нажимаем В наличии:
    page.in_stock.click()
    # нажимаем Ожидаются:
    page.waiting.click()
    # нажимаем Нет в продаже:
    page.out_of_stock.click()
    # нажимаем Показать:
    page.show_button_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'предзаказ' not in title.lower(), msg


# 19 проверка поиска по фильтру-списку НАЛИЧИЕ --> Ожидается
def test_check_waiting_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем НАЛИЧИЕ:
    page.product_stock.click()
    # нажимаем В наличии:
    page.in_stock.click()
    # нажимаем Предзаказ:
    page.pre_order.click()
    # нажимаем Нет в продаже:
    page.out_of_stock.click()
    # нажимаем Показать:
    page.show_button_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'ожидается' not in title.lower(), msg


# 20 проверка поиска по фильтру-списку НАЛИЧИЕ --> Нет в продаже
def test_check_out_of_stock_search_menu(web_browser):
    page = Search(web_browser)
    page.search = 'истори'
    page.search_run_button.click()
    # нажимаем НАЛИЧИЕ:
    page.product_stock.click()
    # нажимаем В наличии:
    page.in_stock.click()
    # нажимаем Предзаказ:
    page.pre_order.click()
    # нажимаем Ожидаются:
    page.waiting.click()
    # нажимаем на Показать:
    page.show_button_stock.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.products_types_not_in_stock.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'нет в продаже' in title.lower(), msg


# 21 проверка поиска по значению в фильтре Авторы
def test_check_author_search(web_browser):
    page = Search(web_browser)
    page.search = 'молот'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # нажимаем Авторы:
    page.authors_button.click()
    # результаты поиска корректные:
    for title in page.authors_names.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'молот' in title.lower(), msg
    # нажимаем первого автора в списке:
    page.our_author_button.click()
    # результаты вывода корректные:
    title = page.page_title.get_text()
    msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
    assert 'молотов игорь игоревич' in title.lower(), msg
    # количество книг корректно:
    assert page.products_titles.count() == 6, 'Количество книг не соотвествует тесту'


# 22 проверка поиска по значению в фильтре Издательства
def test_check_publishing_houses_search(web_browser):
    page = Search(web_browser)
    page.search = 'эком'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # нажимаем Изд-ва:
    page.publishing_offices_button.click()
    # результаты поиска корректные:
    for title in page.publishing_offices.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'эком' in title.lower(), msg
    # нажимаем первое издательство в списке:
    page.publishing_office_button.click()
    # результаты вывода корректные:
    title = page.page_title.get_text()
    msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
    assert 'эком' in title.lower(), msg
    assert page.products_titles_publishing.count() >= 1, 'Не найдено ни одного результата по запросу'


# 23 проверка поиска по значению в фильтре Серии
def test_check_series_search(web_browser):
    page = Search(web_browser)
    page.search = 'избранное'
    page.search_run_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # Нажимаем Серии:
    page.product_series_button.click()
    # результаты поиска корректные:
    for title in page.product_series.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'избранное' in title.lower() or 'избран' in title.lower(), msg
    # нажимаем первую серию в списке:
    page.product_part_button.click()
    # результаты вывода корректные:
    title = page.page_title.get_text()
    msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
    assert 'избранное' in title.lower(), msg
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'


# 24 проверка поиска по значению в фильтре Видео
def test_check_video_search(web_browser):
    page = Search(web_browser)
    page.search = 'избранное'
    page.search_run_button.click()
    # нажимаем Видео:
    page.video_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.video_products.get_attribute('href'):
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert title != '', msg
    for title in page.video_products.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert ('избранное' in title.lower()) or ('избран' in title.lower()), msg


# 25 проверка поиска по значению в фильтре Темы
def test_check_themes_search(web_browser):
    page = Search(web_browser)
    page.search = 'цветы'
    page.search_run_button.click()
    # Нажимаем Темы:
    page.themes_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.themes_products.get_attribute('href'):
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert title != '', msg
    for title in page.themes_products.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'цветы' in title.lower() or 'цвет' in title.lower(), msg
    # нажимаем на первую тему:
    page.theme_button.click()
    # результаты вывода корректные:
    title = page.page_title.get_text()
    msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
    assert 'цветы' in title.lower(), msg


# 26 проверка поиска по значению в фильтре Обзоры
def test_check_reviews_search(web_browser):
    page = Search(web_browser)
    page.search = 'цветы'
    page.search_run_button.click()
    # Нажимаем Темы:
    page.reviews_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.reviews_products.get_attribute('href'):
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert title != '', msg
    for title in page.reviews_products.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'цветы' in title.lower() or 'цвет' in title.lower(), msg


# 27 проверка поиска по значению в фильтре Новости
def test_check_news_search(web_browser):
    page = Search(web_browser)
    page.search = 'цветы'
    page.search_run_button.click()
    # Нажимаем Новости:
    page.news_button.click()
    # найдено не менее одного результата:
    assert page.products_titles.count() >= 1, 'Не найдено ни одного результата по запросу'
    # результаты поиска корректные:
    for title in page.news_products.get_attribute('href'):
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert title != '', msg
    for title in page.news_products.get_text():
        msg = 'Неверный результат поисковой выдачи "{}"'.format(title)
        assert 'цветы' in title.lower() or 'цвет' in title.lower(), msg


# python -m pytest -v --driver Chrome --driver-path C:/pythonProject24/FinalTask_Labirint/chromedriver.exe tests/test_search.py