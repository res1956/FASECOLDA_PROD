#!/usr/local/bin/python
# coding: latin-1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

# Ruta de destino
ruta_destino = sys.argv[1]

# Inicializar el driver de Selenium
driver = webdriver.Chrome()
driver.maximize_window()

# Abre la página web
driver.get("https://guiadevalores.fasecolda.com/ConsultaExplorador/Default.aspx?url=C:\\inetpub\\wwwroot\\Fasecolda\\ConsultaExplorador\\Guias\\GuiaValores_NuevoFormato\\")

# Esperar a que aparezcan todos los elementos que coinciden con el criterio
elementos_enlace = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@class, 'gridViewRow') or contains(@class, 'gridViewAlternateRow')]"))
)

# Obtener el último elemento de la lista
ultimo_elemento = elementos_enlace[-1]

# Desplazarse hasta el último elemento usando JavaScript
driver.execute_script("arguments[0].scrollIntoView(true);", ultimo_elemento)
WebDriverWait(driver, 10).until(
    EC.visibility_of(ultimo_elemento)
)

# Obtener el texto del último elemento
texto_ultimo_elemento = ultimo_elemento.text

# Obtener el ID del último elemento
id_ultimo_elemento = ultimo_elemento.find_element(By.TAG_NAME, "a").get_attribute("id")

# Procesar el texto del último elemento
x = texto_ultimo_elemento.split(" ")  # Empieza en la posición 0
nombre = x[1]
hora = x[4] + " " + x[5] + " " + x[6]

# Escribir los parámetros en un archivo
with open(os.path.join(ruta_destino, "parametros.txt"), "w") as f:
    f.write(id_ultimo_elemento + "|" + nombre + "|" + hora)

print("Archivo grabado")

# Cerrar el driver
driver.quit()
