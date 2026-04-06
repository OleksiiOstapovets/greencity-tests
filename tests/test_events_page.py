import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGreenCity(unittest.TestCase):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity"

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        self.driver.get(self.BASE_URL)
        self.wait = WebDriverWait(self.driver, 10)

        language_switcher = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, "//ul[@aria-label='language switcher']"))
        )
        language_switcher.click()

        en_option = self.wait.until(
        EC.element_to_be_clickable((By.XPATH, ".//span[contains(text(), 'En')]"))
        )
        en_option.click()

    def tearDown(self):
        self.driver.quit()

    # 🔹 Test Case 1
    def test_filter_eco_news_initiatives(self):
        driver = self.driver

        # 1. Перейти в Eco News
        eco_news_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'Eco')]")
        eco_news_tab.click()


        # 2. Обрати Initiatives
        initiatives_filter = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(., 'Initiative')]"))
        )
        initiatives_filter.click()

        # 3. Перевірка (що є новини)
        news_items = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'list')]"))
        )
        self.assertTrue(len(news_items) > 0, "No news displayed for Initiatives filter")


    # 🔹 Test Case 2
    def test_filter_events_upcoming(self):
        driver = self.driver

        # 1. Перейти в Events
        events_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'Events')]")
        events_tab.click()

        # 2. Дочекатися фільтра
        filter = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@class, 'ng-tns')]"))
        )
        filter.click()

        # 3. Обрати Upcoming
        upcoming_filter = driver.find_element(By.XPATH, "//span[contains(text(), 'Upcoming')]")
        upcoming_filter.click()
        # 4. Перевірка (є події)
        events = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'card')]"))
        )
        self.assertTrue(len(events) > 0, "No upcoming events displayed")


    # 🔹 Test Case 3
    def test_ubs_sorting_rules(self):
        driver = self.driver

        # 1. Перейти в UBS Courier
        ubs_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'UBS')]")
        ubs_tab.click()

        # 2. Відкрити правила сортування
        rules_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sorting') and contains(@class, 'url')]"))
        )
        rules_button.click()

        # 3. Перевірка контенту
        rules = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1"))
        )
        self.assertTrue(rules.is_displayed(), "Sorting rules are not displayed")

if __name__ == "__main__":
    unittest.main()