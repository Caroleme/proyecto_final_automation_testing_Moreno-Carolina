from pages.login_page import LoginPage
import pytest
from util.reader import read_users_csv
from util.logger import logger

@pytest.mark.parametrize(
        "data",read_users_csv())
def test_login(driver,data):
    try:
        logger.info("Inicio prueba de login")
        login_page = LoginPage(driver)

        driver.get("https://www.saucedemo.com/")
        logger.info("Ingreso exitoso")

        login_page.login(data["usuario"],data["password"])
        logger.info("Ingreso de credenciales")

        if (data["tipo_usuario"] == "True"):
            assert "/inventory.html" in driver.current_url
            logger.info("Login exitoso")
        elif data["tipo_usuario"] == "False":
            error = login_page.obtener_mensaje_error()
            assert "Epic sadface: Username and password do not match any user in this service" in error
            logger.info("Prueba de mensaje de error valida")
    except Exception:
        logger.exception("Error durante la prueba de login")
        raise

def test_login_campos_vacios(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    
    login_page.login("", "")
    error = login_page.obtener_mensaje_error()
    assert "Epic sadface: Username is required" in error


def test_login_usuario_bloqueado(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.obtener_mensaje_error()
    assert "Epic sadface: Sorry, this user has been locked out." in error


def test_login_campo_contraseña_vacia(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.saucedemo.com/")
    
    login_page.login("standard_user", "")
    error = login_page.obtener_mensaje_error()
    assert "Epic sadface: Password is required" in error