import pytest
import allure
from selenium import webdriver
from pages.home_page import HomePage

@pytest.fixture
def driver():
    with allure.step("Запуск браузера Chrome та відкриття головної сторінки"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.greencity.cx.ua/#/greenCity")
    
    yield driver
    
    with allure.step("Закриття браузера"):
        driver.quit()

@pytest.fixture
def home_page(driver):
    home = HomePage(driver)
    home.switch_to_english()
    return home