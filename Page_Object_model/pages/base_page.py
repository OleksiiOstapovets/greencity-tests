import allure

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent

class BasePage(BaseComponent):

    eco_news_link_locator = (By.XPATH, "//a[contains(text(), 'Eco')]")
    events_link_locator = (By.XPATH, "//a[contains(text(), 'Events')]")
    ubs_link_locator = (By.XPATH, "//a[contains(text(), 'UBS')]")

    language_switcher = (By.XPATH, "//ul[@aria-label='language switcher']")
    language_en_option = (By.XPATH, ".//span[contains(text(), 'En')]")
    language_ua_option = (By.XPATH, ".//span[contains(text(), 'Uk')]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get language switcher")
    def get_language_switcher(self):
        return self._find(*self.language_switcher)
    
    @allure.step("Switch to {language}")
    def switch_language(self, language):
        language_switcher = self.get_language_switcher()
        language_switcher.click()
        if language.lower() == "en":
            language_option = self._find(*self.language_en_option)
        elif language.lower() == "ua":
            language_option = self._find(*self.language_ua_option)
        else:
            raise ValueError("Unsupported language: {}".format(language))
        language_option.click()
        sleep(1)

    @allure.step("Get Eco news button")
    def get_eco_news_button(self):
        return self._find(*self.eco_news_link_locator)
    
    @allure.step("Get Events button")
    def get_events_button(self):
        return self._find(*self.events_link_locator)
    
    @allure.step("Get UBS button")
    def get_ubs_button(self):
        return self._find(*self.ubs_link_locator)

    @allure.step("Navigate to Eco News")
    def navigate_to_eco_news(self):
        eco_news_link = self.get_eco_news_button()
        eco_news_link.click()

    @allure.step("Navigate to Events")
    def navigate_to_events(self):
        events_link = self.get_events_button()
        events_link.click()

    @allure.step("Navigate to UBS")
    def navigate_to_ubs(self):
        ubs_link = self.get_ubs_button()
        ubs_link.click()