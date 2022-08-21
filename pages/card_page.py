import os

from pages.base import WebPage
from pages.elements import WebElement


class CardPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    '''card'''

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
    # Кнопка увеличения количества на 1
    plus_one_more = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')
    # Проверка количества 2
    two_books_in_cart = WebElement(xpath='//input[Compare(test()), "2") and @class="quantity"]')
    # Кнопка удаления из корзины
    remove_from_cart = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')
    # Проверка, что корзина пустая
    empty_cart = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?"]')