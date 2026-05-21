import pytest
import allure
from selenium import webdriver
from pages.base_page import BasePage
from data.config import Config

@pytest.fixture
def driver(scope="function"):
    with allure.step("Launching browser and navigating to Green City"):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Config.BASE_UI_URL)
    
    yield driver
    
    with allure.step("Closing browser"):
        driver.quit()

@pytest.fixture
def base_page(driver):
    base = BasePage(driver)
    base.switch_language("en")
    return base