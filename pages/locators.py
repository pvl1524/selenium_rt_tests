from selenium.webdriver.common.by import By


class AuthLocators:
    # Auth title H1 locator
    AUTH_TITLE = (By.XPATH, "//h1")

    # Tabs locators in Auth Form
    PHONE_TAB = (By.ID, "t-btn-tab-phone")
    EMAIL_TAB = (By.ID, "t-btn-tab-mail")
    LOGIN_TAB = (By.ID, "t-btn-tab-login")
    # LOGIN_TAB = "t-btn-tab-login"
    LS_TAB = (By.ID, "t-btn-tab-ls")

    # Fields locators in Auth Form
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")

    # Login button locator
    LOGIN_BTN = (By.ID, "kc-login")

    # Placeholders locators in Auth Form
    USERNAME_PLACEHOLDER = (By.XPATH, "//input[@id='username']//following-sibling::span")
    PASSWORD_PLACEHOLDER = (By.XPATH, "//input[@id='username']//following-sibling::span")

    # Invalid login or password message locator
    INVALID_LOGIN_OR_PASS_MESSAGE = (By.ID, "form-error-message")

    # Captcha field locator
    CAPTCHA_IMAGE = (By.CSS_SELECTOR, ".rt-captcha__image")
    CAPTCHA_FIELD = (By.ID, "captcha")

    # Register link in Auth Form
    REG_LINK_AUTHFORM = (By.ID, "kc-register")