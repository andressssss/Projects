import pandas as pd
import mysql.connector
import traceback
import readchar

# Configuración de la conexión a la base de datos MySQL
print("Conectando a la BD...")
try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="andresSR",
        passwd="Yy4q9As67jMmK7(/",
        database="infomediagsi"
    )

    consulta_data_cmdb = "SELECT * FROM datacmdbapp"

    print("Generando Excel...")
    
    # Creacion de dataset segunconsulta en la BD
    datacmdb = pd.read_sql_query(consulta_data_cmdb, db_connection)

    # Creacion de archivo XLSX
    datacmdb.to_excel("datacmdb.xlsx", index=False, sheet_name='cmdbdata')
    print("Creacion OK")
    print("Presione cualquier letra para salir")
    k = readchar.readchar()
except:
        print("Ocurrio un error:")
        traceback.print_exc()
        print("Presione cualquier letra para salir")
        k = readchar.readchar()


