from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __int__(self, driver, time=10):
        self.driver = driver
        self.base_url = "https://b2c.passport.rt.ru/"
        self.driver.implicitly_wait(time)

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element_presence(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Not found {locator}")

    def find_element_clickable(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Not found {locator}")
