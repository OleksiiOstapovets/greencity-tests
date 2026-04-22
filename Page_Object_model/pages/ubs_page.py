from selenium.webdriver.common.by import By
from .base_page import BasePage

class UBSPage(BasePage):
    SORTING_RULES_BTN = (By.XPATH, "//a[contains(text(), 'Sorting') and contains(@class, 'url')]")
    TITLE = (By.XPATH, "//h1")

    def open_sorting_rules(self):
        self.click(self.SORTING_RULES_BTN)

    def get_title(self):
        return self.find(self.TITLE)