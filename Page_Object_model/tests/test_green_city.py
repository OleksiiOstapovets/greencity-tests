import pytest
import allure
from pages.base_page import BasePage
from pages.eco_news_page import EcoNewsPage
from pages.events_page import EventsPage
from pages.ubs_page import UBSPage

@allure.epic("Green City Web Interface")
@allure.feature("Content Filtering and Navigation")
class TestGreenCity:

    @allure.title("Filter Eco News by Initiatives")
    @allure.description("Verify that the user can filter news items by the 'Initiative' category on the Eco News page.")
    @allure.tag("Regression", "EcoNews")
    @allure.severity(allure.severity_level.NORMAL)
    def test_filter_eco_news_initiatives(self, driver, base_page):

        home = BasePage(driver)
        home.navigate_to_eco_news()
        
        eco_page = EcoNewsPage(driver)
        eco_page.open_filter_initiatives()
        
        with allure.step("Verify that at least one news item is displayed"):
            news = eco_page.get_news()
            assert len(news) > 0, "No news items found for 'Initiative' filter"

    @allure.title("Filter Upcoming Events")
    @allure.description("Verify that the 'Upcoming' filter correctly displays future events.")
    @allure.tag("Smoke", "Events")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_filter_events_upcoming(self, driver, base_page):
        home = BasePage(driver)
        home.navigate_to_events()
        
        events_page = EventsPage(driver)
        events_page.open_filter()
        events_page.choose_upcoming()
        
        with allure.step("Verify that the list of events is not empty"):
            events = events_page.get_events()
            assert len(events) > 0, "The upcoming events list should not be empty"

    @allure.title("Check UBS Sorting Rules Visibility")
    @allure.description("Navigate to the UBS page and ensure that the 'Sorting Rules' section is accessible and titled correctly.")
    @allure.tag("UBS", "UI")
    def test_ubs_sorting_rules(self, driver, base_page):
        home = BasePage(driver)
        home.navigate_to_ubs()
        
        ubs_page = UBSPage(driver)
        ubs_page.open_sorting_rules()
        
        with allure.step("Verify the visibility of the Sorting Rules title"):
            title = ubs_page.get_title()
            assert title.is_displayed(), "Sorting rules title is not displayed"