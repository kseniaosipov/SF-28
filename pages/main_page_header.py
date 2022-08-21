import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPageHeader(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    '''header'''
    # окно авторизации
    login = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    # кнопка на логотипе-названии
    logo = WebElement(xpath='//*[@class="b-header-b-logo-e-logo-wrap"]')
    # кнопка сообщения
    messages = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[2]/div/ul/li[3]/a/span[1]/span')
    # кнопка Мой Лаб
    my_lab = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[4]/a/span[2]')
    # кнопка Отложено
    postponed = WebElement(xpath='//*[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # кнопка Корзина
    cart = WebElement(xpath='//*[@class="b-header-b-personal-e-list-item have-dropdown  last-child"]')
    # кнопка 18+
    agreement = WebElement(
        xpath='//*[@class="b-header-e-icon-adult b-header-e-icon-adult-m-big b-header-e-sprite-background"]')
    # кнопка Что читать? Рекомендуем
    now = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[1]/div/a[2]/span[2]/span/span')
    # кнопка Книги
    books = WebElement(xpath='//span[@class="b-header-b-menu-e-link top-link-menu first-child"]')
    # кнопка Главное 2022
    best = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[2]/span/a')
    # кнопка Школа
    school = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[3]/span/a')
    # кнопка Игрушки
    games = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[4]/span/a')
    # кнопка Канцтовары
    stationery = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[5]/span/a')
    # кнопка Клуб
    club = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[11]/span/a')
    # кнопка Доставка и оплата
    help = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[1]/a')
    # кнопка Сертификаты
    certificates = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[2]/a')
    # кнопка Рейтинги
    rating = WebElement(xpath='//a[@href="/rating/?id_genre=-1&nrd=1"]')
    # кнопка Новинки
    novelty = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[4]/a')
    # кнопка Скидки
    sale = WebElement(xpath='//a[@href="/sale/"]')
    # кнопка Контакты
    contact = WebElement(xpath='//*[@data-event-content="Контакты"]')
    # кнопка Поддержка
    support = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[10]/a')
    # кнопка 265 пунктов самовывоза
    maps = WebElement(xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div/ul/li[11]/a')

