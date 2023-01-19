import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    yield driver
    driver.quit()