import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.eco_news_page import EcoNewsPage
from pages.events_page import EventsPage
from pages.ubs_page import UBSPage

# Фікстура для керування браузером
@pytest.fixture
def driver():
    # Налаштування (аналог setUp)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.greencity.cx.ua/#/greenCity")
    
    yield driver  # Тут тест отримує драйвер і виконується
    
    # Завершення (аналог tearDown)
    driver.quit()

# Фікстура для ініціалізації головної сторінки та перемикання мови
@pytest.fixture
def home_page(driver):
    home = HomePage(driver)
    home.switch_to_english()
    return home

def test_filter_eco_news_initiatives(driver, home_page):
    home_page.go_to_eco_news()
    eco_page = EcoNewsPage(driver)
    eco_page.filter_initiatives()
    
    news = eco_page.get_news()
    assert len(news) > 0  # У pytest використовуємо звичайний assert

def test_filter_events_upcoming(driver, home_page):
    home_page.go_to_events()
    events_page = EventsPage(driver)
    events_page.open_filter()
    events_page.choose_upcoming()
    
    events = events_page.get_events()
    assert len(events) > 0

def test_ubs_sorting_rules(driver, home_page):
    home_page.go_to_ubs()
    ubs_page = UBSPage(driver)
    ubs_page.open_sorting_rules()
    
    title = ubs_page.get_title()
    assert title.is_displayed()