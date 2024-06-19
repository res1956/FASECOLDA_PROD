from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import zipfile
import sys

archivo_control = sys.argv[1]

f = open(archivo_control, "r")
contenido_archivo_entrada=f.read()
f.close()


x = contenido_archivo_entrada.split("|")
Nombre_directorio_bajada=x[1]
Nombre_id_elemento= x[0].strip()
print (Nombre_id_elemento)

#exit ()
ruta_destino =  sys.argv[2]
chrome_options = Options()

archivos_en_descargas = os.listdir(ruta_destino)

# Eliminar cada archivo en el directorio de descargas
for archivo in archivos_en_descargas:
    try:
        os.remove(os.path.join(ruta_destino, archivo))
        print(f"Se eliminó correctamente el archivo: {archivo}")
    except Exception as e:
        print(f"No se pudo eliminar el archivo {archivo}: {e}")

# Configura las opciones de Chrome
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": ruta_destino,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

# Especifica la ruta al chromedriver y inicializa el navegador
s = Service('C:\\Users\\crisrobles\\Downloads\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.maximize_window()

try:
    # Abre la página web
    driver.get("https://guiadevalores.fasecolda.com/ConsultaExplorador/Default.aspx?url=C:\\inetpub\\wwwroot\\Fasecolda\\ConsultaExplorador\\Guias\\GuiaValores_NuevoFormato\\"+ Nombre_directorio_bajada)
    nombre_archivo = "Guia_Excel"
    # Encuentra el enlace que activa la descarga del archivo mediante su ID
    download_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{nombre_archivo}')]")
    download_link.click()

    # Espera a que la descarga comience
    #time.sleep(30)  # Ajusta según sea necesario

    # Oculta la página mientras se realiza la descarga
    #driver.execute_script("document.body.style.visibility = 'hidden';")

    # Espera a que la descarga se complete
    timeout = 60  # Espera hasta 60 segundos
    nombre_archivo = "Tabla de Homologacion"
    # Encuentra el enlace que activa la descarga del archivo mediante su ID
    download_link = driver.find_element(By.XPATH, f"//a[contains(text(), '{nombre_archivo}')]")
    download_link.click()
    timeout = 60  # Espera hasta 60 segundos
    
    start_time = time.time()
    while True:
        archivos_en_descargas = os.listdir(ruta_destino)
        if any(archivo.endswith('.crdownload') for archivo in archivos_en_descargas):
            if time.time() - start_time > timeout:
                print("Tiempo de espera excedido.")
                break
            time.sleep(1)
        else:
            print("El archivo se ha descargado correctamente.")
            break

finally:
    # Mostrar la página nuevamente
    #driver.execute_script("document.body.style.visibility = 'visible';")

    # Cierra el navegador
    driver.quit()
    print("El navegador se cerró correctamente.")

# Descomprimir el archivo descargado
    for archivo in archivos_en_descargas:
        if archivo.endswith('.zip'):
            ruta_archivo_zip = os.path.join(ruta_destino, archivo)
            with zipfile.ZipFile(ruta_archivo_zip, 'r') as zip_ref:
                zip_ref.extractall(ruta_destino)
            print("El archivo ZIP se ha descomprimido correctamente.")
            # Puedes eliminar el archivo ZIP si lo deseas
            os.remove(ruta_archivo_zip)
