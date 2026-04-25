import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    # Локатори залишаються ті самі...
    LANGUAGE_SWITCHER = (By.XPATH, "//ul[@aria-label='language switcher']")
    EN_OPTION = (By.XPATH, ".//span[contains(text(), 'En')]")
    ECO_TAB = (By.XPATH, "//a[contains(text(), 'Eco')]")
    EVENTS_TAB = (By.XPATH, "//a[contains(text(), 'Events')]")
    UBS_TAB = (By.XPATH, "//a[contains(text(), 'UBS')]")

    @allure.step("Зміна мови на англійську")
    def switch_to_english(self):
        self.click(self.LANGUAGE_SWITCHER)
        self.click(self.EN_OPTION)

    @allure.step("Перехід до розділу Eco News")
    def go_to_eco_news(self):
        self.click(self.ECO_TAB)

    @allure.step("Перехід до розділу Events")
    def go_to_events(self):
        self.click(self.EVENTS_TAB)

    @allure.step("Перехід до розділу UBS")
    def go_to_ubs(self):
        self.click(self.UBS_TAB)