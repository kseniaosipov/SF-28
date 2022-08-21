from pages.main_page_header import MainPageHeader
from selenium.webdriver import ActionChains


'''HEADER'''


# 1 проверка перехода на главную страницу
def test_logo_click(web_browser):
    page = MainPageHeader(web_browser)
    page.logo.click()
    assert page.get_current_url() == 'https://www.labirint.ru/'


# 2 проверка перехода в сообщения
def test_messages_click(web_browser):
    page = MainPageHeader(web_browser)
    page.messages.click()
    assert page.login


# 3 проверка перехода в Мой Лаб
def test_my_lab_click(web_browser):
    page = MainPageHeader(web_browser)
    page.my_lab.click()
    assert page.login


# 4 проверка перехода в Отложено
def test_postponed_click(web_browser):
    page = MainPageHeader(web_browser)
    page.postponed.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


# 5 проверка перехода в Корзина
def test_cart_click(web_browser):
    page = MainPageHeader(web_browser)
    page.cart.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cart/'


# 6 проверка перехода в Пользовательское соглашение (кнопка 18+)
def test_agreement_click(web_browser):
    page = MainPageHeader(web_browser)
    page.agreement.click()
    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'


# 7 проверка перехода в Что читать? Рекомендуем
def test_now_click(web_browser):
    page = MainPageHeader(web_browser)
    page.now.click()
    assert page.get_current_url() == 'https://www.labirint.ru/now/'


# 8 проверка перехода в Книги
def test_books_click(web_browser):
    page = MainPageHeader(web_browser)
    page.books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'


# 9 проверка перехода в Главное 2022
def test_best_click(web_browser):
    page = MainPageHeader(web_browser)
    page.best.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'


# 10 проверка перехода в Школа
def test_school_click(web_browser):
    page = MainPageHeader(web_browser)
    page.school.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/'


# 11 проверка перехода в Игрушки
def test_games_click(web_browser):
    page = MainPageHeader(web_browser)
    page.games.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'


# 12 проверка перехода в Канцтовары
def test_stationery_click(web_browser):
    page = MainPageHeader(web_browser)
    page.stationery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'


# 13 проверка перехода в Клуб
def test_club_click(web_browser):
    page = MainPageHeader(web_browser)
    page.club.click()
    assert page.get_current_url() == 'https://www.labirint.ru/club/'


# 14 проверка перехода в Доставка и оплата
def test_help_click(web_browser):
    page = MainPageHeader(web_browser)
    page.help.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'


# 15 проверка перехода в Сертификаты
def test_certificates_click(web_browser):
    page = MainPageHeader(web_browser)
    page.certificates.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


# 16 проверка перехода в Рейтинги
def test_rating_click(web_browser):
    page = MainPageHeader(web_browser)
    page.rating.click()
    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


# 17 проверка перехода в Новинки
def test_novelty_click(web_browser):
    page = MainPageHeader(web_browser)
    page.novelty.click()
    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


# 18 проверка перехода в Скидки
def test_sale_click(web_browser):
    page = MainPageHeader(web_browser)
    page.sale.click()
    assert page.get_current_url() == 'https://www.labirint.ru/search/' \
                                     '?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


# 19 проверка перехода в Контакты
def test_contact_click(web_browser):
    page = MainPageHeader(web_browser)
    page.contact.click()
    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


# 20 проверка перехода в Поддержка
def test_support_click(web_browser):
    page = MainPageHeader(web_browser)
    page.support.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'


# 21 проверка перехода в 265 унктов самовывоза
def test_maps_click(web_browser):
    page = MainPageHeader(web_browser)
    page.maps.click()
    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


# 22 проверка перехода в соцсеть Вконтакте
def test_vk_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vk = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(vk)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirint_ru'


# 23 проверка перехода в соцсеть Youtube
def test_youtube_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    youtube = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-yt"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(youtube)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


# 24 проверка перехода в соцсеть Одноклассники
def test_ok_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    ok = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-ok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(ok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://ok.ru/labirintru'


# 25 проверка перехода в соцсеть Вконтакте.Дети
def test_vk_kids_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    vk_kids = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-vk-children"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(vk_kids)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintdeti'


# 26 проверка перехода в соцсеть Яндекс.Дзен
def test_dzen_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    dzen = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-zen"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(dzen)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


# 27 проверка перехода в соцсеть Telegram
def test_telegram_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    telegram = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tg"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(telegram)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://t.me/labirintru'


# 28 проверка перехода в соцсеть TikTok
def test_tik_tok_click(web_browser):
    page = MainPageHeader(web_browser)
    social_network = web_browser.find_element_by_xpath(
        '//span[@class="b-header-b-social-e-icon b-header-e-sprite-background '
        'b-header-b-social-e-icon-m-labirint"]')
    tik_tok = web_browser.find_element_by_xpath(
        '//*[@class="b-header-b-social-e-icon b-header-e-sprite-background b-header-b-social-e-icon-m-tiktok"]')
    actions = ActionChains(web_browser)
    actions.move_to_element(social_network)
    actions.click(tik_tok)
    actions.perform()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru'


# python -m pytest -v --driver Chrome --driver-path C:/pythonProject24/FinalTask_Labirint/chromedriver.exe tests/test_main_page_header.py