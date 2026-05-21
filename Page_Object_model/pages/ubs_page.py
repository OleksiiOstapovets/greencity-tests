import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class UBSPage(BasePage):
    Sorting_rules_button_locator = (By.XPATH, "//a[contains(text(), 'Sorting') and contains(@class, 'url')]")
    Title = (By.XPATH, "//h1")

    @allure.step("Get 'Sorting rules' button")
    def get_sorting_rules_button(self):
        return self._find(*self.Sorting_rules_button_locator)

    @allure.step("Open sorting rules")
    def open_sorting_rules(self):
        self.get_sorting_rules_button().click()

    @allure.step("Get page title")
    def get_title(self):
        return self._find(*self.Title)