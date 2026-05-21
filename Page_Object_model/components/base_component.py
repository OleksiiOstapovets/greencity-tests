from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BaseComponent:
    
    def __init__(self, root):
# Якщо root — це вже драйвер, використовуємо його. 
        # Якщо це елемент — беремо драйвер з .parent
        if isinstance(root, WebDriver):
            self.driver = root
            self.node = None # Або driver.find_element(By.TAG_NAME, "html")
        else:
            self.node = root
            self.driver = root.parent
        self.wait = WebDriverWait(self.driver, 10)
    
    def _find(self, by, value=None):
        if value:
        # Якщо прийшло два аргументи (By.XPATH, "selector")
            return self.wait.until(EC.presence_of_element_located((by, value)))
        else:
        # Якщо прийшов один аргумент (кортеж)
            return self.wait.until(EC.presence_of_element_located(by))
    
    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    