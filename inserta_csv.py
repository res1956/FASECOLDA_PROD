import pandas as pd
import pyodbc

# Configura la conex a SQL Server
server = 'sqlm-inbroker-qa-9k4f.d42bbbc966ba.database.windows.net'  # Nombre del servidor o dirección IP
database = 'inbrokerdev'  # Nombre de la base de datos
username = 'user_enaccion'  # Nombre de usuario de SQL Server
password = 'T5rJYgRf23SHxHHHkrgd'  # Contraseña del usuario de SQL Server


# Cadena de conexión a SQL Server
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=' + server + ';'
    'DATABASE=' + database + ';'
    'UID=' + username + ';'
    'PWD=' + password
)

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Leer el archivo CSV con pandas
df = pd.read_csv('g:\\eac\\descargas\\csv\\Guia_Excel_332.csv', sep=';')

# Combinar todas las columnas en una sola columna de texto
df['combined'] = df.apply(lambda row: ';'.join(row.values.astype(str)), axis=1)

# Insertar datos en la tabla
for index, row in df.iterrows():
    cursor.execute(
        "INSERT INTO enaccion.Guia_Excel_332.csv (nombre) VALUES (?)",
        row['combined']
    )

# Confirmar la transacción
conn.commit()

# Cerrar la conexión
cursor.close()
conn.close()
