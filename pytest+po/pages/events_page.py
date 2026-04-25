import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class EventsPage(BasePage):
    FILTER_BUTTON = (By.XPATH, "//*[name()='path' and contains(@class, 'ng-tns')]")
    UPCOMING_FILTER = (By.XPATH, "//span[contains(text(), 'Upcoming')]")
    EVENTS = (By.XPATH, "//div[contains(@class, 'card')]")

    @allure.step("Відкриття фільтра")
    def open_filter(self):
        self.click(self.FILTER_BUTTON)

    @allure.step("Вибір фільтра 'Upcoming'")
    def choose_upcoming(self):
        self.click(self.UPCOMING_FILTER)

    @allure.step("Отримання списку подій")
    def get_events(self):
        return self.finds(self.EVENTS)