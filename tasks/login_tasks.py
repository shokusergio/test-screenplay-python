from pages.login_page import LoginPage
from pages.home_page import HomePage

class LoginTasks:
    """Tareas relacionadas con el login (patrón ScreenPlay)"""
    
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
    
    def navigate_to_login_page(self):
        """Tarea: Navegar a la página de login"""
        self.login_page.navigate()
    
    def perform_login(self, username, password):
        """Tarea: Realizar login con credenciales"""
        self.login_page.enter_username(username)
        self.login_page.enter_password(password)
        self.login_page.click_login_button()
    
    def verify_login_page_loaded(self):
        """Verificación: Página de login cargada correctamente"""
        return self.login_page.is_logo_visible()
    
    def verify_error_message_displayed(self):
        """Verificación: Mensaje de error visible"""
        error_text = self.login_page.get_error_message()
        return "Epic sadface" in error_text or "Username and password do not match" in error_text
    
    def verify_home_page_loaded(self):
        """Verificación: Página Home cargada correctamente"""
        return self.home_page.is_products_title_visible()

