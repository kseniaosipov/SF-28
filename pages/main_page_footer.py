import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPageFooter(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'
        super().__init__(web_driver, url)

    '''footer'''

    # кнопка AppStore
    app_store = WebElement(
        xpath='//*[@class="b-rfooter-e-logo b-rfooter-e-logo-appstore analytics-click-js" '
              'and contains(https://apps.apple.com/ru/app/лабиринт-ру-книжный-магазин/id1008650482")]')

    # кнопка GooglePlay
    google_play = WebElement(
        xpath='//a[@class="b-rfooter-e-section-title b-rfooter-visible-320" '
              'and contains(href(),"https://play.google.com/store/apps/details?id=ru.labirint.android")]')

    # кнопка AppGallery
    app_gallery = WebElement(
        xpath='//a[@class="b-rfooter-e-section-title b-rfooter-visible-320" '
              'and contains(href(),"https://appgallery.cloud.huawei.com/marketshare/app/C101184737")]')

    # кнопка Вконтакте
    vk = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"ВКонтакте")]')

    # кнопка Вконтакте. Дети
    vk_kids = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"ВКонтакте. Дети")]')

    # кнопка Ютьуб
    youtube = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Ютьюб")]')

    # кнопка Одноклассники
    ok = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Одноклассники")]')

    # кнопка Яндекс.Дзен
    dzen = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Дзен")]')

    # кнопка Телеграм
    telegram = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Телеграм")]')

    # кнопка ТикТок
    tik_tok = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"ТикТок")]')

    # кнопка Все книги
    all_books = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Все книги")]')

    # кнопка Школа
    school = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Школа")]')

    # кнопка Журналы
    magazines = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Журналы")]')

    # кнопка Игрушки
    games = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Игрушки")]')

    # кнопка Канцтовары
    office_supplies = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Канцтовары")]')

    # кнопка CD/DVD
    cd_dvd = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"CD/DVD")]')

    # кнопка Сувениры
    souvenirs = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Сувениры")]')

    # кнопка Товары для дома
    household_goods = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Товары для дома")]')

    # кнопка Акции
    sales = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Акции")]')

    # кнопка Главные книги
    main_books = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Главные книги")]')

    # кнопка Бонус за рецензию
    bonus = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Бонус за рецензию")]')

    # кнопка Сертификаты
    certificates = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Сертификаты")]')

    # кнопка Только у нас
    exclusive = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Только у нас")]')

    # кнопка Предзаказы
    pre_order = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Предзаказы")]')

    # кнопка Лабиринт.Сейчас
    lab_now = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Лабиринт. Сейчас")]')

    # кнопка Детский навигатор
    child_now = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Детский навигатор")]')

    # кнопка Рецензии читателей
    reviews = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Рецензии читателей")]')

    # кнопка Книжные обзоры
    book_reviews = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Книжные обзоры")]')

    # кнопка Подборки читателей
    recommendations = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Подборки читателей")]')

    # кнопка Тесты
    lit_tests = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Тесты")]')

    # кнопка Новости Л.
    news = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Новости Л.")]')

    # кнопка Конкурсы
    contests = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Конкурсы")]')

    # кнопка Спепцпроекты
    club = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Спецпроекты")]')

    # кнопка Партнерам
    partner = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Партнерам")]')

    # кнопка Наши вакансии
    job = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Наши вакансии")]')

    # кнопка Войти по коду скидки или через соцсеть
    login_1 = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" '
              'and contains(text(),"Войти по коду скидки или через соцсеть")]')

    # кнопка Вход и регистрация
    login_2 = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Вход и регистрация")]')

    # кнопка Вы смотрели
    visited = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Вы смотрели")]')

    # кнопка Кабинет
    cabinet = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Кабинет")]')

    # окно авторизации
    login = WebElement(
        xpath='//a[@id="g-recap-0-btn"]')

    # кнопка Как сделать заказ
    order_help = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Как сделать заказ")]')

    # кнопка Оплата
    payment = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Оплата")]')

    # кнопка Курьерская доставка
    delivery = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Курьерская доставка")]')

    # кнопка Поддержка
    support = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Поддержка")]')

    # кнопка Напишите нам
    mailto = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Напишите нам")]')

    # кнопка Вся помощь
    help = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" and contains(text(),"Вся помощь")]')

    # кнопка Пользовательское соглашение
    agreement = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link analytics-click-js" '
              'and contains(text(),"Пользовательское соглашение")]')

    # кнопка СтопКовид
    stop_covid = WebElement(
        xpath='//a[@class="sprite_kovid kov_desc"]')

    # кнопка Акит
    akit = WebElement(
        xpath='//a[@class="logo_akit_grey kov_desc"]')

    # кнопка Холдинг «Лабиринт»
    lab_hold = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link b-rfooter-e-item-link-m-small analytics-click-js" '
              'and contains(text(),"© Холдинг «Лабиринт»")]')

    # кнопка 8 800 600-95-25
    contacts = WebElement(
        xpath='//a[@class="b-rfooter-e-item-link b-rfooter-e-item-link-m-small analytics-click-js" '
              'and contains(text(),"8 800 600-95-25")]')
