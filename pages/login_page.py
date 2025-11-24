from selenium.webdriver.common.by import By

class LoginPage:
    """Elementos de la página de Login"""
    
    URL = "https://www.saucedemo.com/"
    
    # Localizadores
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")
    
    def __init__(self, driver):
        self.driver = driver
    
    def navigate(self):
        """Navegar a la página de login"""
        self.driver.get(self.URL)
    
    def is_logo_visible(self):
        """Verificar si el logo de login está visible"""
        return self.driver.find_element(*self.LOGIN_LOGO).is_displayed()
    
    def enter_username(self, username):
        """Ingresar nombre de usuario"""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
    
    def enter_password(self, password):
        """Ingresar contraseña"""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
    
    def click_login_button(self):
        """Hacer clic en el botón de login"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def get_error_message(self):
        """Obtener el mensaje de error"""
        return self.driver.find_element(*self.ERROR_MESSAGE).text
