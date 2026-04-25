import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EcoNewsPage(BasePage):
    INITIATIVES_FILTER = (By.XPATH, "//span[contains(., 'Initiative')]")
    NEWS_ITEMS = (By.XPATH, "//div[contains(@class, 'list')]")
    @allure.step("Відкриття фільтра 'Initiative'")
    def filter_initiatives(self):
        self.click(self.INITIATIVES_FILTER)

    @allure.step("Отримання списку новин")
    def get_news(self):
        return self.finds(self.NEWS_ITEMS)