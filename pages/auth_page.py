from .base_page import BasePage
from .locators import AuthLocators
from pytest_check import check
from twocaptcha import TwoCaptcha


class AuthPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"

    def select_phone_tab(self):
        return self.find_element_presence(AuthLocators.PHONE_TAB).click()

    def select_email_tab(self):
        return self.find_element_presence(AuthLocators.EMAIL_TAB).click()

    def select_login_tab(self):
        return self.find_element_clickable(AuthLocators.LOGIN_TAB).click()

    def select_ls_tab(self):
        return self.find_element_presence(AuthLocators.LS_TAB).click()

    def click_reg_link_on_auth_form(self):
        return self.find_element_clickable(AuthLocators.REG_LINK_AUTHFORM).click()

    def enter_username(self, username):
        username_field = self.find_element_presence(AuthLocators.USERNAME_FIELD)
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)
        return username_field

    def password_field_click(self):
        return self.find_element_presence(AuthLocators.PASSWORD_FIELD).click()

    def enter_password(self, password):
        password_field = self.find_element_presence(AuthLocators.PASSWORD_FIELD)
        # password_field.click()
        password_field.clear()
        password_field.send_keys(password)
        return password_field

    def login_btn_click(self):
        return self.find_element_clickable(AuthLocators.LOGIN_BTN).click()

    def check_login_page_is_open(self):
        check.is_in("https://b2c.passport.rt.ru/",
                    self.driver.current_url), "Incorrect address of the Rostelecom login page"
        check.is_in("Авторизация",
                    self.find_element_presence(AuthLocators.AUTH_TITLE).text), "This is not the Rostelecom login page"
    def check_phone_tab_is_active(self):
        return check.is_in("rt-tab--active", self.find_element_presence(AuthLocators.PHONE_TAB).get_attribute('class')), "The Phone tab is not active."

    def check_email_tab_is_active(self):
        return check.is_in("rt-tab--active", self.find_element_presence(AuthLocators.EMAIL_TAB).get_attribute('class')), "The Email tab is not active."

    def check_login_tab_is_active(self):
        return check.is_in("rt-tab--active", self.find_element_presence(AuthLocators.LOGIN_TAB).get_attribute('class')), "The Login tab is not active."

    def check_account_tab_is_active(self):
        return check.is_in("rt-tab--active", self.find_element_presence(AuthLocators.LS_TAB).get_attribute('class')), "The Account tab is not active."

    def check_invalid_login_or_password__err_on_page(self):
        return check.is_in("Неверный логин или пароль", self.find_element_presence(AuthLocators.INVALID_LOGIN_OR_PASS_MESSAGE).text)

    def captcha(self):
        if "rt-captcha__image" in self.driver.page_source:
            captcha = self.find_element_presence(AuthLocators.CAPTCHA_IMAGE)
            image_captcha = captcha.get_attribute('src')
            solver = TwoCaptcha('a26ca9fc2f0a21a59d3545412cfc8faa')
            result = solver.normal(image_captcha)['code']
            return self.find_element_presence(AuthLocators.CAPTCHA_FIELD).send_keys(result)
        else:
            return False
