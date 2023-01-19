import pytest
from pages.auth_page import AuthPage
from Credentials import Credentials
from pytest_check import check


# Запуск тестов:
# pytest -v --driver Chrome --driver-path chromedriver tests/test_rt_auth.py


@pytest.mark.parametrize("phone", [Credentials.VALID_PHONE, Credentials.INVALID_PHONE], ids=["valid_phone", "invalid_phone"])
@pytest.mark.parametrize("password", [Credentials.VALID_PASSWORD, Credentials.INVALID_PASSWORD], ids=["valid_password", "invalid_password"])
def test_auth_on_phone_tab(phone, password, browser):
    """
    The test checks authorization on the Phone tab in cases of a valid/invalid phone and a valid/invalid password.
    """
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.enter_username(phone)
    page.enter_password(password)
    page.captcha()
    page.login_btn_click()

    if phone == Credentials.VALID_PHONE and password == Credentials.VALID_PASSWORD:
        # Checking that the Accounts page is open
        check.is_in("https://b2c.passport.rt.ru/account_b2c/",
                    browser.current_url), "Incorrect address of the Rostelecom Accounts page"
    else:
        # Verify that user stay at login page
        page.check_login_page_is_open()
        page.check_invalid_login_or_password__err_on_page()


@pytest.mark.parametrize("phones", Credentials.VALID_PHONES)
def test_successful_auth_with_valid_phones_and_password_on_phone_tab(phones, browser):
    page = AuthPage(browser)
    page.go_to_site()

    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.enter_username(phones)
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"


@pytest.mark.parametrize("email", [Credentials.VALID_EMAIL, Credentials.INVALID_EMAIL], ids=["valid_email", "invalid_email"])
@pytest.mark.parametrize("password", [Credentials.VALID_PASSWORD, Credentials.INVALID_PASSWORD], ids=["valid_password", "invalid_password"])
def test_auth_on_email_tab(email, password, browser):
    """
    The test checks authorization on the Email tab in cases of a valid/invalid email and a valid/invalid password.
    """
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_email_tab()
    page.check_email_tab_is_active()

    page.enter_username(email)
    page.enter_password(password)
    page.captcha()
    page.login_btn_click()

    if email == Credentials.VALID_EMAIL and password == Credentials.VALID_PASSWORD:
        # Checking that the Accounts page is open
        check.is_in("https://b2c.passport.rt.ru/account_b2c/",
                    browser.current_url), "Incorrect address of the Rostelecom Accounts page"
    else:
        # Verify that user stay at login page
        page.check_login_page_is_open()
        page.check_invalid_login_or_password__err_on_page()


@pytest.mark.parametrize("logins", Credentials.VALID_LOGINS)
def test_successful_auth_with_valid_logins_and_password_on_login_tab(logins, browser):
    """
    The test checks authorization on the Login tab in cases where there are spaces before and after the login,
    spaces only before the login, and spaces only after the login. The password is valid in all cases.
    """
    page = AuthPage(browser)
    page.go_to_site()

    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_login_tab()
    page.check_login_tab_is_active()

    page.enter_username(logins)
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"


@pytest.mark.parametrize("login", [Credentials.VALID_LOGIN, Credentials.INVALID_LOGIN], ids=["valid_login", "invalid_login"])
@pytest.mark.parametrize("password", [Credentials.VALID_PASSWORD, Credentials.INVALID_PASSWORD], ids=["valid_password", "invalid_password"])
def test__auth_on_login_tab(login, password, browser):
    """
    The test checks authorization on the Login tab in cases of a valid/invalid login and a valid/invalid password.
    """
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_login_tab()
    page.check_login_tab_is_active()

    page.enter_username(login)
    page.enter_password(password)
    page.captcha()
    page.login_btn_click()

    if login == Credentials.VALID_LOGIN and password == Credentials.VALID_PASSWORD:
        # Checking that the Accounts page is open
        check.is_in("https://b2c.passport.rt.ru/account_b2c/",
                    browser.current_url), "Incorrect address of the Rostelecom Accounts page"
    else:
        # Verify that user stay at login page
        page.check_login_page_is_open()
        page.check_invalid_login_or_password__err_on_page()


@pytest.mark.parametrize("account", [Credentials.VALID_LS, Credentials.INVALID_LS], ids=["valid_accout", "invalid_accout"])
@pytest.mark.parametrize("password", [Credentials.VALID_PASSWORD, Credentials.INVALID_PASSWORD], ids=["valid_password", "invalid_password"])
def test__auth_on_account_tab(account, password, browser):
    """
    The test checks authorization on the Account tab in cases of a valid/invalid account and a valid/invalid password.
    """
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_ls_tab()
    page.check_account_tab_is_active()

    page.enter_username(account)
    page.enter_password(password)
    page.captcha()
    page.login_btn_click()

    if account == Credentials.VALID_LS and password == Credentials.VALID_PASSWORD:
        # Checking that the Accounts page is open
        check.is_in("https://b2c.passport.rt.ru/account_b2c/",
                    browser.current_url), "Incorrect address of the Rostelecom Accounts page"
    else:
        # Verify that user stay at login page
        page.check_login_page_is_open()
        page.check_invalid_login_or_password__err_on_page()

def test_successful_auth_with_valid_login_and_password_on_phone_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.enter_username(Credentials.VALID_LOGIN)
    page.password_field_click()
    page.check_login_tab_is_active()
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"

def test_successful_auth_with_valid_login_and_password_on_email_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_email_tab()
    page.check_email_tab_is_active()

    page.enter_username(Credentials.VALID_LOGIN)
    page.password_field_click()
    page.check_login_tab_is_active()
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"

def test_successful_auth_with_valid_eamel_and_password_on_account_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_ls_tab()
    page.check_account_tab_is_active()

    page.enter_username(Credentials.VALID_EMAIL)
    page.password_field_click()
    page.check_email_tab_is_active()
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"

def test_successful_auth_with_valid_account_and_password_on_email_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_email_tab()
    page.check_email_tab_is_active()

    page.enter_username(Credentials.VALID_LS)
    page.password_field_click()
    page.check_account_tab_is_active()
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Checking that the Accounts page is open
    check.is_in("https://b2c.passport.rt.ru/account_b2c/", browser.current_url), "Incorrect address of the Rostelecom Accounts page"

def test_unsuccessful_auth_with_valid_email_and_invalid_password_on_phone_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    # If Phone is not selected ckick on it
    page.select_phone_tab()
    page.check_phone_tab_is_active()

    page.enter_username(Credentials.VALID_EMAIL)
    page.password_field_click()
    page.check_email_tab_is_active()
    page.enter_password(Credentials.INVALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Verify that user stay at login page
    page.check_login_page_is_open()

    page.check_invalid_login_or_password__err_on_page()

def test_unsuccessful_auth_with_invalid_email_and_valid_password_on_phone_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    # If Phone is not selected ckick on it
    page.select_phone_tab()
    page.check_phone_tab_is_active()

    page.enter_username(Credentials.INVALID_EMAIL)
    page.password_field_click()
    page.check_email_tab_is_active()
    page.enter_password(Credentials.VALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Verify that user stay at login page
    page.check_login_page_is_open()

    page.check_invalid_login_or_password__err_on_page()

def test_successful_open_reg_page_from_auth_form_by_clicking_register_link(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.click_reg_link_on_auth_form()

    # Checking that the Registration page is open
    check.is_in("/registration", browser.current_url), "Incorrect address of the Registration page"

def test_unsuccessful_auth_with_invalid_email_and_invalid_password_on_phone_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    # If Phone is not selected ckick on it
    page.select_phone_tab()
    page.check_phone_tab_is_active()

    page.enter_username(Credentials.INVALID_EMAIL)
    page.password_field_click()
    page.check_email_tab_is_active()
    page.enter_password(Credentials.INVALID_PASSWORD)
    page.captcha()
    page.login_btn_click()

    # Verify that user stay at login page
    page.check_login_page_is_open()
    page.check_invalid_login_or_password__err_on_page()

def test_select_phone_tab_with_valid_phone_on_account_tab(browser):
    page = AuthPage(browser)

    page.go_to_site()
    page.check_login_page_is_open()
    # Phone tab is active by default
    page.check_phone_tab_is_active()

    page.select_ls_tab()
    page.check_account_tab_is_active()

    page.enter_username(Credentials.VALID_PHONE)
    page.password_field_click()
    page.check_phone_tab_is_active()

