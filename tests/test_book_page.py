from pages.book_page import BookPage

'''Book page'''


# Заходим в карточку и добавляем в корзину
def test_add_best_book_to_cart(web_browser):
    page = BookPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    assert page.successfully_ordered


# Заходим в карточку и добавляем в отложенные
def test_add_best_book_to_deferred(web_browser):
    page = BookPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_deferred.click()
    page.deferred.click()
    assert page.successfully_deferred


# Заходим в карточку и добавляем к сравнению
def test_add_best_book_to_comparison(web_browser):
    page = BookPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()
    assert page.successfully_compared


# Заходим на страницу сравнения
def test_compare_books(web_browser):
    page = BookPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()
    page.logo.click()
    page.random_book_other.click()
    page.compare.click()
    page.compare_books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/compare/'
    assert "2" in page.count_span.get_text()


# python -m pytest -v --driver Chrome --driver-path C:/pythonProject24/FinalTask_Labirint/chromedriver.exe  tests/test_book_page.py