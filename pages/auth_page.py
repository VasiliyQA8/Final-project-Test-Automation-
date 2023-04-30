from pages.locators import AuthLocators
from pages.base_page import BasePage
import ast

class AuthPage(BasePage):
    def get_text_from_page(self, LOCATOR):
        return self.find_elements(LOCATOR)[0].text

    def click_user_agreement_link_and_privacy_policy(self, LOCATOR):
        return self.find_element(LOCATOR).click()

    def login_using_social_networks(self, LOCATOR):
        return self.find_element(LOCATOR).click()

    def click_on_auth_type_selection_menu(self, LOCATOR):
        return self.find_element(LOCATOR).click()

    def active_input_form_placeholder(self):
        return self.find_element(AuthLocators.AUTH_PAGE_INPUT_PLACEHOLDER).text

    def active_auth_type(self):
        return self.find_element(AuthLocators.AUTH_ACTIVE_TYPE).text

    def password_input_form_placeholder(self):
        return self.find_element(AuthLocators.PASSWORD_INPUT_FORM_PLACEHOLDER).text

    def clickable_eye_in_input_form(self):
        return self.find_element_until_to_be_clickable(AuthLocators.EYE_IN_INPUT_FORM)

    def forgot_my_password_link(self):
        return self.find_element(AuthLocators.FORGOT_MY_PASSWORD)

    def on_off_checkbox(self):
        return self.find_element(AuthLocators.OFF_ON_CHECKBOX)

    def get_error_message(self):
        return self.find_element(AuthLocators.ERROR_MESSAGE).text

    def enter_username(self, value):
        username = self.find_element(AuthLocators.INPUT_USERNAME)
        username.send_keys(value)

    def enter_password(self, value):
        password = self.find_element(AuthLocators.INPUT_PASS)
        password.send_keys(value)

    def login_button(self):
        self.find_element(AuthLocators.LOGIN_BUTTON).click()

    def check_color(self, element):
        rgba = element.value_of_css_property('color')
        r, g, b, alpha = ast.literal_eval(rgba.strip('rgba'))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        return hex_value


