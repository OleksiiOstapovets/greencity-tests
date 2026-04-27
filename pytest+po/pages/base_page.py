import allure

from selenium.webdriver.common.by import By
from time import sleep


class BasePage:

    eco_news_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Еко новини') or contains(., 'Eco news')]")
    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    eco_news_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Еко новини') or contains(., 'Eco news')]")
    events_link_locator = (By.XPATH, "//header//a[contains(@class, 'url-name') and contains(., 'Події') or contains(., 'Events')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Get Eco news button")
    def get_eco_news_button(self):
        return self.driver.find_element(*self.eco_news_link_locator)