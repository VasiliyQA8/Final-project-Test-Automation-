from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы страницы авторизации"""
    PAGE_NAME = (By.CSS_SELECTOR, ".card-container__title")
    SELECTION_MENU = (By.CSS_SELECTOR, "div.rt-tabs.rt-tabs--orange.rt-tabs--small")
    AUTH_ACTIVE_TYPE = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    AUTH_PAGE_INPUT_PLACEHOLDER = (By.CSS_SELECTOR, '.rt-input__placeholder')
    BTN_MAIL = (By.ID, 't-btn-tab-mail')
    BTN_LOGIN = (By.ID, 't-btn-tab-login')
    BTN_LS = (By.ID, 't-btn-tab-ls')
    BTN_TELEPHONE = (By.ID, 't-btn-tab-phone')
    PASSWORD_INPUT_FORM_PLACEHOLDER = (By.XPATH, '//span[contains(text(), "Пароль")]')
    LEFT_SIDE_OF_PAGE = (By.ID, 'page-left')
    EYE_IN_INPUT_FORM = (By.CSS_SELECTOR, 'svg.rt-base-icon.rt-base-icon--fill-path.rt-eye-icon')
    INPUT_USERNAME = (By.ID, 'username')
    INPUT_PASS = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'kc-login')
    FOOTER_TEXT = (By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]')
    USER_AGREEMENT_LINK = (By.PARTIAL_LINK_TEXT, 'пользовательского соглашения')
    USER_AGREEMENT_LINK_IN_FOOTER = (By.PARTIAL_LINK_TEXT, 'Пользовательским соглашением')
    PRIVACY_POLICY_LINK_IN_FOOTER = (By.PARTIAL_LINK_TEXT, 'Политикой конфиденциальности')
    FORGOT_MY_PASSWORD = (By.ID, 'forgot_password')
    CHECKBOX_REMEMBER_ME = (By.XPATH, "//*[@class='rt-checkbox__label']")
    OFF_ON_CHECKBOX = (By.XPATH, '//div[contains(@class, "rt-checkbox")]')
    LINK_VK = (By.ID, 'oidc_vk')
    LINK_ODNOKLASSNIKI = (By.ID, 'oidc_ok')
    LINK_MAILRU = (By.ID, 'oidc_mail')
    LINK_GOOGLE = (By.ID, 'oidc_google')
    LINK_YANDEX = (By.XPATH, '//a[5]')
    ERROR_MESSAGE = (By.XPATH, "//span[@id='form-error-message']")
    AUTH_REG_IN = (By.XPATH, "//a[@id='kc-register']")
    AUTH_REG_IN_TEMP_CODE = (By.ID, 'back_to_otp_btn')



class RegLocators:
    """Локаторы страницы регистрации"""
    PAGE_NAME = (By.CSS_SELECTOR, ".card-container__title")


