#  Proyecto Final de Automatización QA - Sauce Demo - Carolina Moreno

## Descripcion

Este repositorio contiene un framework de automatización de pruebas híbrido desarrollado en Python utilizando Pytest y Selenium WebDriver. Su objetivo principal es validar de forma integral tanto la experiencia de usuario (UI) en los flujos críticos del sitio web Sauce Demo (como el inicio de sesión, inventario y gestión del carrito de compras) como la integración y respuesta de servicios web (API REST) utilizando ReqRes.

## Tecnologias usadas

El stack tecnológico seleccionado es el siguiente: 

- Lenguaje: Python
- Automatización de Navegador Web: Selenium WebDriver
- Framework: Pytest
- Reportes: Pytest HTML
- Control de versiones: Git
- Requests: Consumo y validación de endpoints de API REST.

## Instalacion y Configuración

## Clonar Repositorio: 

`git clone https://github.com/Caroleme/proyecto_final_automation_testing_Moreno-Carolina.git`


## Estructura del Proyecto

El repositorio está organizado de forma modular aplicando el patrón Page Object Model (POM):

Proyecto_Final_AutomatizacionQA/

├── data/
│   ├── products.json        # Datos de productos para pruebas
│   └── users.csv            # Datos parametrizados de usuarios para login
│
├── logs                     # Archivos de registro (logs) de ejecución del framework
│
├── pages/
│   ├── cart_page.py         # Page Object para la vista del carrito de compras     
│   ├── inventory_page.py    # Page Object para la vista de inventario
│   └── login_page.py        # Page Object para la vista de inicio de sesión
│
├── reports/
│   └── reporte.html         # Reportes HTML generados por Pytest
│   └── screenshots          # Capturas de pantalla de evidencias ante fallos
│
├── test/
│   ├── test_api.py          # Pruebas de API REST (ReqRes)
│   ├── test_car.py          # Pruebas del carrito de compras
│   ├── test_inventory.py    # Pruebas de UI del inventario
│   └── test_login.py        # Pruebas parametrizadas de inicio de sesión
│
├── util/
│   ├── logger.py            # Configuración de logs del framework
│   └── reader.py            # Lectores de archivos CSV y JSON
│
├── conftest.py              # Fixtures globales de Pytest (driver, login)
├── guia.md
├── pytest.ini               # Configuración general de Pytest
└── requirements.txt         # Dependencias del proyecto


## Instalacion dependencias

`pip install -r requirements.txt`

## Ejecucion de todas las  Pruebas:

python -m pytest

## Ejecucion de Pruebas especificas:

py -m pytest -v test/test_inventory.py

## Funcionamiento de las pruebas

- Test cart: Realiza el flujo completo de agregar productos al carrito, verifica el contador, valida el nombre del primer producto y de que el producto seleccionado coincida con el que aparece.

- Test login: Valida el ingreso al sitio web Sauce Demo con credenciales válidas

- Test inventory: Este test verifica que el titulo de la página sea el correcto (Swag Labs), que existan productos visibles en la página y elementos importantes de la interfaz, como menu, filtro y carrito.

- Test api: Este test verifica el funcionamiento de las Apis con los metodos GET, POST; DELETE basadas en el estándar de 5 niveles de validación Status Code, Headers, Estructura JSON, Contenido de los datos y Rendimiento.

## Generar Reporte HTML:

python -m pytest --html=report.html

