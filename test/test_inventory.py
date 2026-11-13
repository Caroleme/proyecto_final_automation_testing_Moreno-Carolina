
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_title(login_in_driver):
    """Título usando la fixture con login"""
    driver = login_in_driver
    titulo = driver.title
    assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"

def test_productos_visibles(login_in_driver):
    """Productos visibles usando Page Object"""
    driver = login_in_driver
    inventory_page = InventoryPage(driver)
    productos = inventory_page.obtener_productos()
    assert len(productos) > 0, "No hay productos visibles"

def test_ui_menu(login_in_driver):
    """Valida el Menú"""
    driver = login_in_driver
    inventory_page = InventoryPage(driver)
    assert inventory_page.menu_visible(), "El icono del menu no está presente en la pagina"

def test_ui_filtro(login_in_driver):
    """Valida el Filtro"""
    driver = login_in_driver
    inventory_page = InventoryPage(driver)
    assert inventory_page.filtro_visible(), "El filtro del catalogo no está presente en la pagina"

def test_inventory(login_in_driver):
    """Valida la información detallada del segundo producto con su precio"""
    driver = login_in_driver
    inventory_page = InventoryPage(driver)

    productos = inventory_page.obtener_productos()
    assert len(productos) > 0

    assert inventory_page.obtener_nombre_segundo_producto() == "Sauce Labs Bike Light"
    assert inventory_page.obtener_precio_segundo_producto() == "$9.99"

    assert inventory_page.menu_visible()
    assert inventory_page.filtro_visible()
