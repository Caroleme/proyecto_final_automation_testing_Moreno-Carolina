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

```text
proyecto_final_automation_testing_Moreno-Carolina/
├── .github/
│   └── workflows/
│       └── test.yml
├── data/
├── logs/
├── pages/
├── reports/
├── test/
├── util/
├── conftest.py
├── guia.md
├── pytest.ini
├── readme.md
└── requirements.txt```

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

