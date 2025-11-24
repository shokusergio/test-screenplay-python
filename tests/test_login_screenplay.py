import sys
import os
# Agregar el directorio padre al path para que Python encuentre los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tasks.login_tasks import LoginTasks
import time

class TestLoginScreenPlay:
    """Tests automatizados End to End usando patrón ScreenPlay"""
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Configuración antes y después de cada test"""
        # Setup: Iniciar el navegador
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.login_tasks = LoginTasks(self.driver)
        
        yield  # Aquí se ejecuta el test
        
        # Teardown: Cerrar el navegador
        time.sleep(2)  # Pausa para ver el resultado
        self.driver.quit()
    
    def test_1_validar_ingreso_a_la_pagina(self):
        """
        Test 1: Validar el ingreso a la ruta de la web 
        y que exista un assert de un componente en la pantalla login
        """
        # Navegar a la página
        self.login_tasks.navigate_to_login_page()
        
        # ASSERT: Verificar que el logo de login está visible
        assert self.login_tasks.verify_login_page_loaded(), \
            "ERROR: El logo de la página de login no está visible"
        
        print("✓ Test 1 PASÓ: La página de login cargó correctamente")
    
    def test_2_validar_login_con_credenciales_fallidas(self):
        """
        Test 2: Validar Login por credenciales fallidas 
        y debe tener un ASSERT que valide el error mostrado en la pantalla
        """
        # Navegar a la página
        self.login_tasks.navigate_to_login_page()
        
        # Intentar login con credenciales incorrectas
        self.login_tasks.perform_login("usuario_incorrecto", "password_incorrecto")
        
        # ASSERT: Verificar que aparece mensaje de error
        assert self.login_tasks.verify_error_message_displayed(), \
            "ERROR: No se mostró el mensaje de error esperado"
        
        print("✓ Test 2 PASÓ: Se validó correctamente el error de credenciales incorrectas")
    
    def test_3_validar_login_correcto(self):
        """
        Test 3: Validar Login correcto utilizando credenciales válidas,
        el assert debe validar un componente en la página Home
        """
        # Navegar a la página
        self.login_tasks.navigate_to_login_page()
        
        # Realizar login con credenciales correctas
        self.login_tasks.perform_login("standard_user", "secret_sauce")
        
        # ASSERT: Verificar que estamos en la página Home
        assert self.login_tasks.verify_home_page_loaded(), \
            "ERROR: No se cargó correctamente la página Home después del login"
        
        print("✓ Test 3 PASÓ: Login exitoso y página Home cargada correctamente")
