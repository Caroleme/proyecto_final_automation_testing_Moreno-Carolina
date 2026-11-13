
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from util.reader import read_productos_json

def test_cart(login_in_driver):
    driver = login_in_driver

    # Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    # Verificar contador carrito
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "La cantidad de productos no se agregaron correctamente"

    # Obtener nombre del primer producto
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    # Verificar el producto agregado en el carrito
    assert cart_item == product_name, "El producto agregado no coincide"

    # Seguir comprando

    # Hacer clic en el botón "Continue Shopping" para regresar al inventario
    driver.find_element(By.ID, "continue-shopping").click()

    # Verificar que regresó exitosamente a la página de inventario
    assert "inventory.html" in driver.current_url, "El botón 'Continue Shopping' no redirigió al inventario"



    