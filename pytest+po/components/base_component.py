from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from selenium.webdriver.support.ui import EC

class BaseComponent:
    
    def __init__(self, root:WebElement):
        self.node = root
        self.driver = root.parent
    
    def _find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    