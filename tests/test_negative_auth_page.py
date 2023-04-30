import pytest
from pages.auth_page import *
from settings import *


@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_invalid_email_and_invalid_pass(browser):
    '''Авторизация по почте и паролю (невалидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_MAIL)
    page.enter_username(invalid_email)
    page.enter_password(invalid_password)
    page.login_button()
    assert page.get_error_message() == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    assert page.check_color(page.forgot_my_password_link()) == '#ff4f12'  # элемент "Забыл пароль" перекрашен в оранжевый цвет

@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_invalid_login_and_invalid_pass(browser):
    '''Авторизация по логину и паролю (невалидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_LOGIN)
    page.enter_username(invalid_login)
    page.enter_password(invalid_password)
    page.login_button()
    assert page.get_error_message() == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    assert page.check_color(page.forgot_my_password_link()) == '#ff4f12'  # элемент "Забыл пароль" перекрашен в оранжевый цвет

@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_invalid_email_and_valid_pass(browser):
    '''Авторизация по почте и паролю (невалидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_MAIL)
    page.enter_username(invalid_email)
    page.enter_password(valid_password)
    page.login_button()
    assert page.get_error_message() == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    assert page.check_color(page.forgot_my_password_link()) == '#ff4f12'  # элемент "Забыл пароль" перекрашен в оранжевый цвет

@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
def test_auth_with_invalid_login_and_valid_pass(browser):
    '''Авторизация по логину и паролю (невалидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_LOGIN)
    page.enter_username(invalid_login)
    page.enter_password(valid_password)
    page.login_button()
    assert page.get_error_message() == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    assert page.check_color(page.forgot_my_password_link()) == '#ff4f12'  # элемент "Забыл пароль" перекрашен в оранжевый цвет


@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
@pytest.mark.parametrize('password', ['      _qQ', 'qwertyQ', mix, russian_chars(), '12345678',
                                      'rtkid_168', english_chars().upper()]
    , ids=['6spaces+_+qQ', '7symbols', 'mix', 'russian', '8digit', 'str(lowercase)+special+digit', 'capital letters only'])
def test_auth_with_valid_email_and_invalid_pass(browser, password):
    '''Авторизация по почте(валидные данные) и паролю(невалидный набор данных) '''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_MAIL)
    page.enter_username(valid_email)
    page.enter_password(password)
    page.login_button()
    assert page.get_error_message() == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'


@pytest.mark.auth
@pytest.mark.xfail(reason='CAPTCHA')   #Из-за капчи ожидаем, что тест будет падать.
@pytest.mark.parametrize('username', ['         _Q', 'q', mix, generate_string_en(256), russian_chars(),
                                      '123456789101', 'rtkid_1689900', old_valid_ls]
    , ids=['9spaces+_+Q', 'symbol', 'mix', '256 symbols', 'russian', 'digit', 'str(en)+special+digit', 'old_LS'])
def test_auth_with_invalid_LS_data(browser, username):
    '''Авторизация по ЛС(невалидные данные + old_valid_ls(корректный ЛС,
    но нерабочий/старый)) и паролю (валидные данные)'''
    page = AuthPage(browser)
    page.go_to_site()
    page.click_on_auth_type_selection_menu(AuthLocators.BTN_LS)
    page.enter_username(username)
    page.enter_password(valid_password)
    page.login_button()
    assert page.get_error_message() or 'Неверно введен текст с картинки' == 'Неверный логин или пароль'

