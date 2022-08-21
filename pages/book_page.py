import os

from pages.base import WebPage
from pages.elements import WebElement


class BookPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    '''book page'''

    # кнопка Лучшая покупка дня
    best_sale = WebElement(xpath='//*[@href="/best/sale/"]')
    # кнопка Акционного товара
    random_book = WebElement(xpath='//*[@id="catalog"]/div/div[3]/div/div[4]/div/div[1]/div/div[1]/div/div[1]')
    # кнопка В корзину
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    # кнопка Корзина
    cart = WebElement(xpath='//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]')
    # Проверка, что заказ появился
    successfully_ordered = WebElement(xpath='//span[contains(text(),"Ваш заказ")]')
    # кнопка Добавить в отложенные
    add_to_deferred = WebElement(xpath='//a[@class="fave"]')
    # Кнопка Отложено
    deferred = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # Кнопка Выделить все
    successfully_deferred = WebElement(xpath='//a[@title="Выделить все отложенные товары"]')
    # Кнопка Добавить к сравнению
    compare = WebElement(xpath='//a[@title="Добавить к сравнению"]')
    # Успешно добавлен к сравнению
    successfully_compared = WebElement(xpath='//*[@class="compare big-compare done"]')
    # Кнопка Главная страница
    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    # Кнопка книги
    random_book_other = WebElement(xpath='//*[@id="right-inner"]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[1]/a[2]')
    # Кнопка Сравнить
    compare_books = WebElement(xpath='//a[@href="/compare/"]')
    # Кнопка числа добаленных к сравнению
    count_span = WebElement(xpath='//span[@class="compare-button__num"]')