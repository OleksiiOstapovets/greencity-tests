import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EcoNewsPage(BasePage):
    filter_initiatives_locator = (By.XPATH, "//span[contains(., 'Initiative')]")
    News = (By.XPATH, "//div[contains(@class, 'list')]")
    
    @allure.step("Get 'Initiative' filter")
    def get_filter_initiatives(self):
        return self._find(*self.filter_initiatives_locator)

    @allure.step("Open 'Initiative' filter")
    def open_filter_initiatives(self):
        self.get_filter_initiatives().click()

    @allure.step("Get news list")
    def get_news(self):
        return self.finds(self.News)