import pandas as pd
import mysql.connector
import readchar
import traceback

ruta_docs = ("C:/Users/Usuario/Documents/Back UP/Infomedia/Requerimientos/MySQL/Cruce/")

try:
    # Lectura del excel - tabla eventos
    print("Leyendo excel origen...")
    dexcel = pd.read_excel(ruta_docs + "dataGSI.xlsx", sheet_name="eventos", header=0)

    # Creacion CSV eventos
    print("Convirtiendo tabla eventos...")
    dexcel.to_csv(ruta_docs + "CSV/eventos.csv", index = False)

    # Reset del dataframe
    del dexcel

    # Lectura del excel - tabla CMDB
    print("Leyendo excel origen...")
    dexcel = pd.read_excel(ruta_docs + "dataGSI.xlsx", sheet_name="cmdb", header=0)

    # Creacion CSV cmdb
    print("Convirtiendo tabla cmdb...")
    dexcel.to_csv(ruta_docs + "CSV/cmdb.csv", index = False)

    # Reset del dataframe
    del dexcel

    # Lectura del excel - tabla lb
    print("Leyendo excel origen...")
    dexcel = pd.read_excel(ruta_docs + "dataGSI.xlsx", sheet_name="lb", header=0)

    # Creacion CSV lineabase
    print("Convirtiendo tabla lineabase...")
    dexcel.to_csv(ruta_docs + "CSV/lb.csv", index = False)

    # Reset del dataframe
    del dexcel


    # Configuración de la conexión a la base de datos MySQL
    print("Conectando a la BD...")
    db_connection = mysql.connector.connect(
        host="localhost",
        user="andresSR",
        passwd="Yy4q9As67jMmK7(/",
        database="infomediagsi"
    )
    cursor = db_connection.cursor()

    print("Vaciando las tablas...")
    vaciar_tabla_eventos = ("TRUNCATE TABLE dataeventosapp")
    vaciar_tabla_cmdb = ("TRUNCATE TABLE datacmdbapp")
    vaciar_tabla_lb = ("TRUNCATE TABLE datalbapp")

    plantilla_consulta = ("LOAD DATA INFILE '" +  ruta_docs + "CSV/")

    cargar_data_eventos = (plantilla_consulta + "eventos.csv' INTO TABLE dataeventosapp FIELDS TERMINATED BY ',' ENCLOSED BY '\n'IGNORE 1 ROWS")
    cargar_data_cmdb = (plantilla_consulta + "cmdb.csv' INTO TABLE datacmdbapp FIELDS TERMINATED BY ',' ENCLOSED BY '\n'IGNORE 1 ROWS")
    cargar_data_lb = (plantilla_consulta + "lb.csv' INTO TABLE datalbapp FIELDS TERMINATED BY ',' ENCLOSED BY '\n'IGNORE 1 ROWS")

    # Cargar los datos en la tabla de la base de datos
    print("Cargando data a las tbalas...")
    cursor.execute(vaciar_tabla_eventos)
    cursor.execute(vaciar_tabla_cmdb)
    cursor.execute(vaciar_tabla_lb)
    cursor.execute(cargar_data_eventos)
    cursor.execute(cargar_data_cmdb)
    cursor.execute(cargar_data_lb)


    db_connection.commit()
    cursor.close()
    db_connection.close()
    print("Carga OK")
    print("Presione cualquier letra para salir")
    k = readchar.readchar()
except:
    print("Ocurrio un error:")
    traceback.print_exc()
    print("Presione cualquier letra para salir")
    k = readchar.readchar()
