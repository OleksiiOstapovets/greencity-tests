import unittest
import allure
from selenium import webdriver
from pages.base_page import BasePage
from pages.eco_news_page import EcoNewsPage
from pages.events_page import EventsPage
from pages.ubs_page import UBSPage
from data.config import Config

@allure.epic("Green City Web Interface")
@allure.feature("Content Filtering and Navigation")
class TestGreenCity(unittest.TestCase):

    def setUp(self):
        """Аналог фікстур driver та base_page з Pytest. 
        Виконується перед кожним окремим тестом."""
        with allure.step("Launching browser and navigating to Green City"):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get(Config.BASE_UI_URL)
        
        # Логіка з колишньої фікстури base_page
        self.base_page = BasePage(self.driver)
        self.base_page.switch_language("en")

    def tearDown(self):
        """Аналог блоку yield driver з Pytest.
        Виконується після кожного окремого тесту."""
        with allure.step("Closing browser"):
            self.driver.quit()

    @allure.title("Filter Eco News by Initiatives")
    @allure.description("Verify that the user can filter news items by the 'Initiative' category on the Eco News page.")
    @allure.tag("Regression", "EcoNews")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_eco_news_initiatives(self):
        # Використовуємо self.driver та self.base_page замість аргументів
        home = BasePage(self.driver)
        home.navigate_to_eco_news()
        
        eco_page = EcoNewsPage(self.driver)
        eco_page.open_filter_initiatives()
        
        with allure.step("Verify that at least one news item is displayed"):
            news = eco_page.get_news()
            # Замінено assert на self.assertGreater
            self.assertGreater(len(news), 0, "No news items found for 'Initiative' filter")

    @allure.title("Filter Upcoming Events")
    @allure.description("Verify that the 'Upcoming' filter correctly displays future events.")
    @allure.tag("Smoke", "Events")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filter_events_upcoming(self):
        home = BasePage(self.driver)
        home.navigate_to_events()
        
        events_page = EventsPage(self.driver)
        events_page.open_filter()
        events_page.choose_upcoming()
        
        with allure.step("Verify that the list of events is not empty"):
            events = events_page.get_events()
            # Замінено assert на self.assertGreater
            self.assertGreater(len(events), 0, "The upcoming events list should not be empty")

    @allure.title("Check UBS Sorting Rules Visibility")
    @allure.description("Navigate to the UBS page and ensure that the 'Sorting Rules' section is accessible and titled correctly.")
    @allure.tag("UBS", "UI")
    def test_ubs_sorting_rules(self):
        home = BasePage(self.driver)
        home.navigate_to_ubs()
        
        ubs_page = UBSPage(self.driver)
        ubs_page.open_sorting_rules()
        
        with allure.step("Verify the visibility of the Sorting Rules title"):
            title = ubs_page.get_title()
            # Замінено assert на self.assertTrue
            self.assertTrue(title.is_displayed(), "Sorting rules title is not displayed")

if __name__ == "__main__":
    unittest.main()