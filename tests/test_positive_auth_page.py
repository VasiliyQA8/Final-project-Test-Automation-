from time import sleep
import pytest
from pages.auth_page import AuthPage
from settings import *
from pages.locators import AuthLocators, RegLocators

@pytest.mark.ui
def test_loading_auth_page(browser):
    '''Загрузка главной страницы сайта https://b2c.passport.rt.ru. Проверка заголовка страницы "Авторизация"'''
    page = AuthPage(browser)
    page.go_to_site()
    name_page = page.get_text_from_page(AuthLocators.PAGE_NAME)
    assert 'https://b2c.passport.rt.ru/auth' in browser.current_url
    assert name_page == "Авторизация"

@pytest.mark.ui
def test_type_selection_menu(browser):
    '''Меню выбора типа аутентификации содержит в правой части страницы:
    1. Выбор аутентификации по мобильному телефону, "Телефон"
    2. Выбор аутентификации по электронной почте и паролю, "Почта"
    3. Выбор аутентификации по логину и паролю, "Логин"
    4. Выбор аутентификации по лицевому счету и паролю, “Лицевой счет”'''
    page = AuthPage(browser)
    page.go_to_site()
    elements_menu = page.get_text_from_page(AuthLocators.SELECTION_MENU).split()
    assert 'Телефон', 'Почта' in elements_menu
    assert 'Логин', 'Лицевой' in elements_menu

@pytest.mark.ui
def test_input_form_is_selected_by_default(browser):
    '''По умолчанию выбрана форма авторизации по Мобильному телефону'''
    page = AuthPage(browser)
    page.go_to_site()
    name_placeholder = page.active_input_form_placeholder()
    assert name_placeholder == 'Мобильный телефон'

@pytest.mark.ui
def test_active_auth_type(browser):
    '''Все элементы меню выбора аутентификации кликабельны("Телефон", "Почта", "Логин", “Лицевой счет”).
    При клике на элемент меню аутентификации происходит смена поля ввода соответсующее элементу меню.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_MAIL)  #Клик по кнопке "Почта"
    name_active_placeholder = page.active_input_form_placeholder()
    name_active_auth_type = page.active_auth_type()
    assert name_active_auth_type, name_active_placeholder == 'Почта' "Электронная почта"
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_LOGIN)   #Клик по кнопке "Логин"
    name_active_placeholder_1 = page.active_input_form_placeholder()
    name_active_auth_type_1 = page.active_auth_type()
    assert name_active_auth_type_1, name_active_placeholder_1 == 'Логин' 'Логин'
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_LS)     #Клик по кнопке “Лицевой счет”
    name_active_placeholder_2 = page.active_input_form_placeholder()
    name_active_auth_type_2 = page.active_auth_type()
    assert name_active_auth_type_2, name_active_placeholder_2 == 'Лицевой счёт' 'Лицевой счёт'
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_TELEPHONE)   #Клик по кнопке "Телефон"
    name_active_placeholder_3 = page.active_input_form_placeholder()
    name_active_auth_type_3 = page.active_auth_type()
    assert name_active_auth_type_3, name_active_placeholder_3 == 'Телефон' 'Мобильный телефон'

@pytest.mark.ui
def test_password_entry_form(browser):
    '''Проверка страницы Авторизации на содержание формы ввода "Пароль" в правой части
    и кликабельность в форме ввода иконки-глаза (скрыть/показать) пароль'''
    page = AuthPage(browser)
    page.go_to_site()
    name_placeholder = page.password_input_form_placeholder()
    assert name_placeholder == 'Пароль'
    assert page.clickable_eye_in_input_form()

@pytest.mark.ui
def test_page_left_title(browser):
    '''Проверка страницы Авторизации на содержание заголовка "Личный кабинет" и дополнительной информации
    в левой части страницы.'''
    page = AuthPage(browser)
    page.go_to_site()
    On_left_side_of_page = page.get_text_from_page(AuthLocators.LEFT_SIDE_OF_PAGE)
    assert 'Личный кабинет' in On_left_side_of_page
    assert 'Персональный помощник в цифровом мире Ростелекома' in On_left_side_of_page


@pytest.mark.ui
@pytest.mark.xfail
@pytest.mark.parametrize('username', [valid_login, valid_email, valid_phone, old_valid_ls],
                         ids=['login', 'email', 'phone', 'ls'])
def test_automatic_change_of_auth_selection(browser, username):
    """Проверка автоматического переключения типов авторизации тел/почта/логин/ЛС.
    В автоматическом режиме переключения не происходит"""
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(username)
    if username == valid_login:
        assert page.active_auth_type() == 'Логин'
    else:
        print('В автоматическом режиме переключения не происходит')
    if username == valid_email:
        assert page.active_auth_type() == 'Почта'
    else:
        print('В автоматическом режиме переключения не происходит')
    if username == valid_phone:
        assert page.active_auth_type() == 'Телефон'
    else:
        print('В автоматическом режиме переключения не происходит')
    if username == old_valid_ls:
        assert page.active_auth_type() == 'Лицевой счёт'
    else:
        print('В автоматическом режиме переключения не происходит')

@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_valid_email(browser):
    '''Авторизация по почте и паролю (валидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(valid_email)
    page.enter_password(valid_password)
    page.login_button()
    assert page.get_relative_link() == '/account_b2c/page'

@pytest.mark.ui
@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_valid_login(browser):
    '''Авторизация по логину и паролю (валидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_username(valid_login)
    page.enter_password(valid_password)
    page.login_button()
    assert page.get_relative_link() == '/account_b2c/page'
    sleep(1)         #Задержка нужна для прогона тестов

@pytest.mark.ui
def test_link_forgot_password(browser):
    '''Cсылка "Забыл пароль" переход на страницу восcтановления пороля.
     Проверка заголовка страницы "Восстановление пароля"'''
    page = AuthPage(browser)
    page.go_to_site()
    page.forgot_my_password_link().click()
    name_page = page.get_text_from_page(RegLocators.PAGE_NAME)
    assert name_page == "Восстановление пароля"

@pytest.mark.ui
def test_checkbox_remember_me(browser):
    '''Чекбокс "Запомнить меня" - кликабельность'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.CHECKBOX_REMEMBER_ME) #Клик по Чекбоксу
    off_checkbox = page.on_off_checkbox().get_dom_attribute("class")  #Чекбокс выключен
    assert off_checkbox != 'rt-checkbox rt-checkbox--checked' #Чекбокс включен


@pytest.mark.ui
def test_consent_to_the_processing_of_personal_data_and_Links_Privacy_Policy(browser):
    '''Проверка страницы Авторизации на содержание информации о согласии на обработку персональных данных
    и кликабельные ссылки на Политику конфиденциальности и Пользовательское соглашение.'''
    page = AuthPage(browser)
    page.go_to_site()
    footer_text = page.get_text_from_page(AuthLocators.FOOTER_TEXT)
    assert 'Продолжая использовать наш сайт, вы даете согласие на обработку' in footer_text
    page.click_user_agreement_link_and_privacy_policy(AuthLocators.USER_AGREEMENT_LINK)      #Клик на ссылку
    # "пользовательского соглашения" под кнопкой "Войти"
    browser.switch_to.window(browser.window_handles[1])
    sleep(1)
    assert browser.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    sleep(1)
    page.click_user_agreement_link_and_privacy_policy(AuthLocators.USER_AGREEMENT_LINK_IN_FOOTER)   #Клик на ссылку
    # "Пользовательским соглашением" в подвале/футер
    browser.switch_to.window(browser.window_handles[1])
    sleep(1)
    assert browser.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    page.click_user_agreement_link_and_privacy_policy(AuthLocators.PRIVACY_POLICY_LINK_IN_FOOTER)   #Клик на ссылку
    # "Политикой конфиденциальности" в подвале/футер
    browser.switch_to.window(browser.window_handles[1])
    sleep(1)
    assert browser.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


@pytest.mark.ui
@pytest.mark.social_networks
def test_redirect_link_VK(browser):
    '''При клике на ссылку/кнопку "В Контакте" происходит переход на соответствующую страницу.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.login_using_social_networks(AuthLocators.LINK_VK)
    assert 'https://oauth.vk.com/authorize' in browser.current_url

@pytest.mark.ui
@pytest.mark.social_networks
def test_redirect_link_ODNOKLASSNIKI(browser):
    '''При клике на ссылку/кнопку "Одноклассники" происходит переход на соответствующую страницу.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.login_using_social_networks(AuthLocators.LINK_ODNOKLASSNIKI)
    assert 'https://connect.ok.ru/dk?st.cmd=OAuth2Login&st.redirect' in browser.current_url

@pytest.mark.ui
@pytest.mark.social_networks
def test_redirect_link_Mailru(browser):
    '''При клике на ссылку/кнопку "Mail.ru" происходит переход на соответствующую страницу.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.login_using_social_networks(AuthLocators.LINK_MAILRU)
    assert 'https://connect.mail.ru/oauth/authorize' in browser.current_url

@pytest.mark.ui
@pytest.mark.social_networks
def test_redirect_link_Google(browser):
    '''При клике на ссылку/кнопку "Google" происходит переход на соответствующую страницу.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.login_using_social_networks(AuthLocators.LINK_GOOGLE)
    assert 'https://accounts.google.com' in browser.current_url

@pytest.mark.ui
@pytest.mark.social_networks
@pytest.mark.xfail(reason='yandexdriver.exe') #В Yandex браузере ожидаем, что тест будет падать.
def test_redirect_link_Yandex(browser):
    '''При клике на ссылку/кнопку "Яндекс" происходит переход на соответствующую страницу.'''
    page = AuthPage(browser)
    page.go_to_site()
    page.login_using_social_networks(AuthLocators.LINK_YANDEX)
    assert 'https://oauth.yandex.ru/authorize' or 'https://passport.yandex.ru/auth' in browser.current_url
