import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EventsPage(BasePage):
    Filter_button_locator = (By.XPATH, "//*[name()='path' and contains(@class, 'ng-tns')]")
    Upcoming_filter_button_locator = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    Events = (By.XPATH, "//div[contains(@class, 'card')]")

    @allure.step("Get filter button")
    def get_filter_button(self):
        return self._find(*self.Filter_button_locator)

    @allure.step("Open filter")
    def open_filter(self):
        self.get_filter_button().click()

    @allure.step("Get 'Upcoming' filter button")
    def get_upcoming_filter_button(self):
        return self._find(*self.Upcoming_filter_button_locator)

    @allure.step("Choose 'Upcoming' filter")
    def choose_upcoming(self):
        self.get_upcoming_filter_button().click()

    @allure.step("Get events list")
    def get_events(self):
        return self.finds(self.Events)