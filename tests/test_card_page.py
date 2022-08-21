from pages.card_page import CardPage

'''Card'''


# Добавление Книги в корзину
def test_add_book_to_cart(web_browser):
    page = CardPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    assert page.successfully_ordered


# Увеличиваем количество книг на 1
def test_make_more_books_in_cart(web_browser):
    page = CardPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.plus_one_more.click()
    assert page.two_books_in_cart


# Удаляем книги
def test_remove_book_from_cart(web_browser):
    page = CardPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.remove_from_cart.click()
    assert page.empty_cart

# python -m pytest -v --driver Chrome --driver-path C:/pythonProject24/FinalTask_Labirint/chromedriver.exe tests/test_card_page.py
