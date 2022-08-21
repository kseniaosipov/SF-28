from pages.main_page_body import MainPageBody


'''Body'''


# 1 проверка перехода в Что почитать: выбор редакции
def test_check_what_to_read(web_browser):
    page = MainPageBody(web_browser)
    page.what_to_read_button.click()
    assert page.products_titles_large.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/top/toread/'
    assert page.page_title.get_text() == "Что почитать: выбор редакции"


# 2 проверка перехода в Лучшая покупка дня
def test_check_best_buy(web_browser):
    page = MainPageBody(web_browser)
    page.best_buy_button.click()
    assert page.products_carts.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'
    title = page.page_title.get_text()
    assert 'главные книги' in title.lower()


# 3 проверка перехода в Больше книг со скидками
def test_check_discounts_books(web_browser):
    page = MainPageBody(web_browser)
    page.discounts_button.click()
    assert page.products_carts.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/best/sale/'
    for title in page.discounts_books.get_text():
        msg = 'Неправильный результат поиска "{}"'.format(title)
        assert '%' in title, msg
    title = page.page_title.get_text()
    assert 'главные книги' in title.lower()


# 4 проверка перехода в Читатели выбирают сегодня
def test_check_today(web_browser):
    page = MainPageBody(web_browser)
    page.today_button.click()
    assert page.products_books_now.count() >= 1
    title = page.page_title.get_text()
    assert 'главные книги' in title.lower()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'


# 5 проверка перехода в Лабиринт. Сейчас
def test_check_button_now(web_browser):
    page = MainPageBody(web_browser)
    page.now_button.click()
    title = page.active_menu_item.get_text()
    assert 'лабиринт. сейчас' in title.lower()
    assert page.get_current_url() == 'https://www.labirint.ru/now/'


# 6 проверка перехода в Детский навигатор — что читать детям и с детьми
def test_check_button_kids(web_browser):
    page = MainPageBody(web_browser)
    page.kids_button.click()
    title = page.active_menu_item.get_text()
    assert 'детский навигатор' in title.lower()
    assert page.get_current_url() == 'https://www.labirint.ru/child-now/'


# 7 проверка перехода в Книжные лидеры продаж
def test_check_button_leaders(web_browser):
    page = MainPageBody(web_browser)
    page.leaders_button.click()
    title = page.page_title.get_text()
    assert 'рейтинг продаж' in title.lower()
    assert page.products_books_leaders.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?period=2&id_genre=1852'


# 8 проверка перехода в Книги: новинки 2022
def test_check_button_novelties_books(web_browser):
    page = MainPageBody(web_browser)
    page.novelties_books_button.click()
    title = page.page_title.get_text()
    assert 'новые книги' in title.lower()
    assert page.products_books_new.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


# 9 проверка перехода в Книжные обзоры и рецензии
def test_check_button_reviews(web_browser):
    page = MainPageBody(web_browser)
    page.reviews_button.click()
    title = page.heading_reviews.get_text()
    assert 'обзоры и рецензии' in title.lower()
    assert page.products_reviews.count() >= 1
    assert page.get_current_url() == 'https://www.labirint.ru/news/books/'


# 10 проверка перехода по кнопке Правила в разделе Вам подарок
def test_check_button_regulations(web_browser):
    page = MainPageBody(web_browser)
    page.regulations_button.click()
    title = page.page_title.get_text()
    assert 'купон' in title.lower()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?cardhelp=2300'


# python -m pytest -v --driver Chrome --driver-path C:/pythonProject24/FinalTask_Labirint/chromedriver.exe tests/test_main_page_body.py
