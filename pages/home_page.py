from selenium.webdriver.common.by import By

class HomePage:
    """Elementos de la página Home"""
    
    # Localizadores
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    
    def __init__(self, driver):
        self.driver = driver
    
    def is_products_title_visible(self):
        """Verificar si el título de productos está visible"""
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()
    
    def get_products_title_text(self):
        """Obtener el texto del título de productos"""
        return self.driver.find_element(*self.PRODUCTS_TITLE).text
