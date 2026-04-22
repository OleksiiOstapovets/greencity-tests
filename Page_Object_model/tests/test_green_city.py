import sys
import os
# Get the path to the parent directory (Page_Object_model)
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(parent_dir)
import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.eco_news_page import EcoNewsPage
from pages.events_page import EventsPage
from pages.ubs_page import UBSPage

class TestGreenCity(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

        self.home = HomePage(self.driver)
        self.home.switch_to_english()

    def tearDown(self):
        self.driver.quit()

    # 🔹 Test 1
    def test_filter_eco_news_initiatives(self):
        self.home.go_to_eco_news()

        eco_page = EcoNewsPage(self.driver)
        eco_page.filter_initiatives()

        news = eco_page.get_news()
        self.assertTrue(len(news) > 0)

    # 🔹 Test 2
    def test_filter_events_upcoming(self):
        self.home.go_to_events()

        events_page = EventsPage(self.driver)
        events_page.open_filter()
        events_page.choose_upcoming()

        events = events_page.get_events()
        self.assertTrue(len(events) > 0)

    # 🔹 Test 3
    def test_ubs_sorting_rules(self):
        self.home.go_to_ubs()

        ubs_page = UBSPage(self.driver)
        ubs_page.open_sorting_rules()

        title = ubs_page.get_title()
        self.assertTrue(title.is_displayed())


if __name__ == "__main__":
    unittest.main()