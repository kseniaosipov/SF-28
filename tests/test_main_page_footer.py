from pages.main_page_footer import MainPageFooter


# 1 проверка перехода на приложение в AppStore
def test_app_store_click(web_browser):
    page = MainPageFooter(web_browser)
    page.app_store.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://apps.apple.com/ru/app/лабиринт-ру-книжный-магазин/id1008650482'


# 2 проверка перехода на приложение в GooglePlay
def test_google_play_click(web_browser):
    page = MainPageFooter(web_browser)
    page.google_play.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://play.google.com/store/apps/details?id=ru.labirint.android'


# 3 проверка перехода на приложение в AppGallery
def test_app_gallery_click(web_browser):
    page = MainPageFooter(web_browser)
    page.app_gallery.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://appgallery.cloud.huawei.com/marketshare/app/C101184737'


# 4 проверка перехода в соцсеть Вконтакте
def test_vk_click(web_browser):
    page = MainPageFooter(web_browser)
    page.vk.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirint_ru'


# 5 проверка перехода в соцсеть Вконтакте.Дети
def test_vk_kids_click(web_browser):
    page = MainPageFooter(web_browser)
    page.vk_kids.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://vk.com/labirintdeti'


# 6 проверка перехода в соцсеть Youtube
def test_youtube_click(web_browser):
    page = MainPageFooter(web_browser)
    page.youtube.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.youtube.com/user/labirintruTV'


# 7 проверка перехода в соцсеть Одноклассники
def test_ok_click(web_browser):
    page = MainPageFooter(web_browser)
    page.ok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://ok.ru/labirintru'


# 8 проверка перехода в соцсеть Яндекс.Дзен
def test_dzen_click(web_browser):
    page = MainPageFooter(web_browser)
    page.dzen.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://zen.yandex.ru/labirintru'


# 9 проверка перехода в соцсеть Telegram
def test_telegram_click(web_browser):
    page = MainPageFooter(web_browser)
    page.telegram.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://t.me/labirintru'


# 10 проверка перехода в соцсеть TikTok
def test_tik_tok_click(web_browser):
    page = MainPageFooter(web_browser)
    page.tik_tok.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    assert page.get_current_url() == 'https://www.tiktok.com/@labirintru'


# 11 проверка перехода в Все книги
def test_all_books_click(web_browser):
    page = MainPageFooter(web_browser)
    page.all_books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/books/'


# 12 проверка перехода в Школа
def test_school_click(web_browser):
    page = MainPageFooter(web_browser)
    page.school.click()
    assert page.get_current_url() == 'https://www.labirint.ru/school/?price_min=&price_max=&discount=1'


# 13 проверка перехода в Журналы
def test_magazines_click(web_browser):
    page = MainPageFooter(web_browser)
    page.magazines.click()
    assert page.get_current_url() == 'https://www.labirint.ru/journals/'


# 14 проверка перехода в Игрушки
def test_games_click(web_browser):
    page = MainPageFooter(web_browser)
    page.games.click()
    assert page.get_current_url() == 'https://www.labirint.ru/games/'


# 15 проверка перехода в Канцтовары
def test_office_supplies_click(web_browser):
    page = MainPageFooter(web_browser)
    page.office_supplies.click()
    assert page.get_current_url() == 'https://www.labirint.ru/office/'


# 16 проверка перехода в CD/DVD
def test_cd_dvd_click(web_browser):
    page = MainPageFooter(web_browser)
    page.cd_dvd.click()
    assert page.get_current_url() == 'https://www.labirint.ru/multimedia/'


# 17 проверка перехода в Сувениры
def test_souvenirs_click(web_browser):
    page = MainPageFooter(web_browser)
    page.souvenirs.click()
    assert page.get_current_url() == 'https://www.labirint.ru/souvenir/'


# 18 проверка перехода в Товары для дома
def test_household_goods_click(web_browser):
    page = MainPageFooter(web_browser)
    page.household_goods.click()
    assert page.get_current_url() == 'https://www.labirint.ru/household/'


# 19 проверка перехода в Акции
def test_sales_click(web_browser):
    page = MainPageFooter(web_browser)
    page.sales.click()
    assert page.get_current_url() == 'https://www.labirint.ru/actions/'


# 20 проверка перехода в Главные книги
def test_main_books_click(web_browser):
    page = MainPageFooter(web_browser)
    page.main_books.click()
    assert page.get_current_url() == 'https://www.labirint.ru/best/'


# 21 проверка перехода в Бонус за рецензию
def test_bonus_click(web_browser):
    page = MainPageFooter(web_browser)
    page.bonus.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/bonus-za-recenziyu/'


# 22 проверка перехода в Сертификаты
def test_certificates_click(web_browser):
    page = MainPageFooter(web_browser)
    page.certificates.click()
    assert page.get_current_url() == 'https://www.labirint.ru/certificates/'


# 23 проверка перехода в Только у нас
def test_exclusive_click(web_browser):
    page = MainPageFooter(web_browser)
    page.exclusive.click()
    assert page.get_current_url() == 'https://www.labirint.ru/certificates/'


# 24 проверка перехода в Предзаказы
def test_pre_order_click(web_browser):
    page = MainPageFooter(web_browser)
    page.pre_order.click()
    assert page.get_current_url() == 'https://www.labirint.ru/top/skoro-v-prodazhe/'


# 25 проверка перехода в Лабиринт.Сейчас
def test_lab_now_click(web_browser):
    page = MainPageFooter(web_browser)
    page.lab_now.click()
    assert page.get_current_url() == 'https://www.labirint.ru/now/'


# 26 проверка перехода в Детский навигатор
def test_child_now_click(web_browser):
    page = MainPageFooter(web_browser)
    page.child_now.click()
    assert page.get_current_url() == 'https://www.labirint.ru/child-now/'


# 27 проверка перехода в Рецензии читателей
def test_reviews_click(web_browser):
    page = MainPageFooter(web_browser)
    page.reviews.click()
    assert page.get_current_url() == 'https://www.labirint.ru/reviews/'


# 28 проверка перехода в Книжные обзоры
def test_book_reviews_click(web_browser):
    page = MainPageFooter(web_browser)
    page.book_reviews.click()
    assert page.get_current_url() == 'https://www.labirint.ru/news/books/'


# 29 проверка перехода в Подборки читателей
def test_recommendations_click(web_browser):
    page = MainPageFooter(web_browser)
    page.recommendations.click()
    assert page.get_current_url() == 'https://www.labirint.ru/recommendations/'


# 30 проверка перехода в Тесты
def test_lit_tests_click(web_browser):
    page = MainPageFooter(web_browser)
    page.lit_tests.click()
    assert page.get_current_url() == 'https://www.labirint.ru/recommendations/'


# 31 проверка перехода в Новости Л.
def test_news_click(web_browser):
    page = MainPageFooter(web_browser)
    page.news.click()
    assert page.get_current_url() == 'https://www.labirint.ru/news/'


# 32 проверка перехода в Конкурсы
def test_contests_click(web_browser):
    page = MainPageFooter(web_browser)
    page.contests.click()
    assert page.get_current_url() == 'https://www.labirint.ru/contests/'


# 33 проверка перехода в Спепцпроекты
def test_club_click(web_browser):
    page = MainPageFooter(web_browser)
    page.club.click()
    assert page.get_current_url() == 'https://www.labirint.ru/club/'


# 34 проверка перехода в Партнерам
def test_partner_click(web_browser):
    page = MainPageFooter(web_browser)
    page.partner.click()
    assert page.get_current_url() == 'https://partner.labirint.ru/login'


# 35 проверка перехода в Наши вакансии
def test_job_click(web_browser):
    page = MainPageFooter(web_browser)
    page.job.click()
    assert page.get_current_url() == 'https://www.labirint.org/vakansii?tab=5'


# 36 проверка перехода в Войти по коду скидки или через соцсеть
def test_login_1_click(web_browser):
    page = MainPageFooter(web_browser)
    page.login_1.click()
    assert page.login


# 37 проверка перехода в Вход и регистрация
def test_login_2_click(web_browser):
    page = MainPageFooter(web_browser)
    page.login_2.click()
    assert page.login


# 38 проверка перехода в Вы смотрели
def test_visited_click(web_browser):
    page = MainPageFooter(web_browser)
    page.visited.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/?vybor=visited'


# 39 проверка перехода в Кабинет
def test_cabinet_click(web_browser):
    page = MainPageFooter(web_browser)
    page.cabinet.click()
    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/'


# 40 проверка перехода в Как сделать заказ
def test_order_help_click(web_browser):
    page = MainPageFooter(web_browser)
    page.order_help.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/order/'


# 41 проверка перехода в Оплата
def test_payment_click(web_browser):
    page = MainPageFooter(web_browser)
    page.payment.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?clause=132'


# 42 проверка перехода в Курьерская доставка
def test_delivery_click(web_browser):
    page = MainPageFooter(web_browser)
    page.delivery.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/?clause=9'


# 43 проверка перехода в Поддержка
def test_support_click(web_browser):
    page = MainPageFooter(web_browser)
    page.support.click()
    assert page.get_current_url() == 'https://www.labirint.ru/support/'


# 44 проверка перехода в Вся помощь
def test_help_click(web_browser):
    page = MainPageFooter(web_browser)
    page.help.click()
    assert page.get_current_url() == 'https://www.labirint.ru/help/'


# 45 проверка перехода в Пользовательское соглашение
def test_agreement_click(web_browser):
    page = MainPageFooter(web_browser)
    page.agreement.click()
    assert page.get_current_url() == 'https://www.labirint.ru/agreement/'


# 46 проверка перехода в СтопКовид
def test_stop_covid_click(web_browser):
    page = MainPageFooter(web_browser)
    page.stop_covid.click()
    assert page.get_current_url() == 'https://ecomvscovid.ru/'


# 47 проверка перехода в Акит
def test_akit_click(web_browser):
    page = MainPageFooter(web_browser)
    page.akit.click()
    assert page.get_current_url() == 'https://www.labirint.ru/#'


# 48 проверка перехода в Холдинг «Лабиринт»
def test_lab_hold_click(web_browser):
    page = MainPageFooter(web_browser)
    page.lab_hold.click()
    assert page.get_current_url() == 'https://www.labirint.org/'


# 49 проверка перехода в 8 800 600-95-25
def test_contacts_click(web_browser):
    page = MainPageFooter(web_browser)
    page.contacts.click()
    assert page.get_current_url() == 'https://www.labirint.ru/contact/'

# python -m pytest -v --driver Chrome --driver-path С:/pythonProject24/FinalTask_Labirint/chromedriver.exe  tests/test_main_page_footer.py
