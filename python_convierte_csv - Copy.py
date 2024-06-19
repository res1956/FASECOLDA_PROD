import os
import pandas as pd
import glob
import re
import sys

# Directorio donde se encuentran los archivos Excel#
directorio_excel = sys.argv[1]

# Directorio donde se guardarán los archivos CSV
directorio_csv = sys.argv[2]

f = open(os.path.join(directorio_csv, "archivos_a_procesar.txt"), "w")
f.write("Nombres\n")

# Patrones para los nombres de archivo
patron_guia_excel = re.compile(r'Guia_Excel_\d+\.xls')
patron_tabla_homologacion = re.compile(r'Tabla de Homologacion \d+\.xlsx')

# Obtener la lista de nombres de archivo de Excel en el directorio
archivos_excel = glob.glob(os.path.join(directorio_excel, '*.xls*'))

# Iterar sobre cada archivo Excel
for archivo_excel in archivos_excel:
    # Obtener el nombre del archivo sin la ruta
    nombre_archivo = os.path.basename(archivo_excel)
    
    print("NOMBRE: ", nombre_archivo)
    f.write(nombre_archivo.split('.')[0] + '.csv\n')

    # Comprobar si el nombre del archivo coincide con el patrón de Guia_Excel_???
    if patron_guia_excel.match(nombre_archivo):
        # Leer el archivo Excel con Pandas
        try:
            df = pd.read_excel(archivo_excel, sheet_name='Codigos')
            
            # Verificar el contenido del DataFrame
            print("Contenido del DataFrame antes de guardarlo:")
            print(df.head())

            # Generar el nombre de archivo CSV
            nombre_archivo_csv = os.path.join(directorio_csv, "excel.csv")
            
            # Asegurarse de que no hay valores nulos que causen problemas
            df.fillna('', inplace=True)

            # Restablecer el índice si es necesario
            df.reset_index(drop=True, inplace=True)
            
            # Guardar el DataFrame como un archivo CSV con encabezados (para depuración)
            df.to_csv(nombre_archivo_csv, index=False, header=True, sep=";")
            print(f"Se ha convertido la hoja 'Codigos' de {nombre_archivo} a CSV con encabezados para depuración.")
        except Exception as e:
            print(f"No se pudo procesar el archivo {nombre_archivo}: {e}")
    
    # Comprobar si el nombre del archivo coincide con el patrón de Tabla de Homologacion ???
    elif patron_tabla_homologacion.match(nombre_archivo):
        # Leer el archivo Excel con Pandas
        try:
            df = pd.read_excel(archivo_excel)
            
            # Verificar el contenido del DataFrame
            print("Contenido del DataFrame antes de guardarlo:")
            print(df.head())

            # Generar el nombre de archivo CSV
            nombre_archivo_csv = os.path.join(directorio_csv, f"{nombre_archivo.split('.')[0]}.csv")
            
            # Asegurarse de que no hay valores nulos que causen problemas
            df.fillna('', inplace=True)

            # Restablecer el índice si es necesario
            df.reset_index(drop=True, inplace=True)
            
            # Guardar el DataFrame como un archivo CSV con encabezados (para depuración)
            df.to_csv(nombre_archivo_csv, index=False, header=True, sep=";")
            print(f"Se ha convertido el archivo {nombre_archivo} a CSV con encabezados para depuración.")
        except Exception as e:
            print(f"No se pudo procesar el archivo {nombre_archivo}: {e}")
    
    else:
        print(f"No se procesó el archivo {nombre_archivo}.")

f.close()
print("La conversión de Excel a CSV se ha completado.")
