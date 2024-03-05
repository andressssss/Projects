from docx2pdf import convert
import pandas as pd
import mysql.connector
import traceback
import readchar
import time
import subprocess

ruta_ws = "C:/Users/Usuario/Servicio Nacional de Aprendizaje/TELEFONICA - Infraestructura Centralizada/Soluciones GSI/SERVICIOS WEB/"
ruta_ht = "C:/Users/Usuario/Servicio Nacional de Aprendizaje/TELEFONICA - Infraestructura Centralizada/Soluciones GSI/HERRAMIENTAS/"
ruta_si = "C:/Users/Usuario/Servicio Nacional de Aprendizaje/TELEFONICA - Infraestructura Centralizada/Soluciones GSI/SISTEMAS DE INFORMACION/"
ruta_pap = "C:/Users/Usuario/Servicio Nacional de Aprendizaje/SENA - Infraestructura Centralizada (1)/Soluciones GSI PAP/Soluciones existentes/"

total_fallos = []

def countdown_timer(seconds):
    while seconds > 0:
        print(f"por favor espere: {seconds} segundos", end="\r")
        time.sleep(1)  # Delay for 1 second
        seconds -= 1

    print("Siguiente operacion...:")

try:
    # Configuración de la conexión a la base de datos MySQL
    print("Conectando a la BD...")
    db_connection = mysql.connector.connect(
        host="localhost",
        user="andresSR",
        passwd="Yy4q9As67jMmK7(/",
        database="infomediagsi"
    )
    
    print("Consultando listado de aplicaciones...")
    consulta_lista_app_WS = "SELECT * FROM listadoapp WHERE ubicacion = 'N/A' AND codigo LIKE '%WS%'"
    consulta_lista_app_HT = "SELECT * FROM listadoapp WHERE ubicacion = 'N/A' AND codigo LIKE '%HT%'"
    consulta_lista_app_SI = "SELECT * FROM listadoapp WHERE ubicacion = 'N/A' AND codigo LIKE '%SI%'"
    consulta_lista_app_PAP = "SELECT * FROM listadoapp WHERE ubicacion = 'PAP'"

    # Creacion de dataset segunconsulta en la BD
    dataapp_ws = pd.read_sql_query(consulta_lista_app_WS, db_connection)
    dataapp_ht = pd.read_sql_query(consulta_lista_app_HT, db_connection)
    dataapp_si = pd.read_sql_query(consulta_lista_app_SI, db_connection)
    dataapp_pap = pd.read_sql_query(consulta_lista_app_PAP, db_connection)

    print("Generando Documentos...")

    # Creacion de PDF con codigo WS ---------------------------------------------------------------------------------------------------------------------------------------------
    for index, row in dataapp_ws.iterrows():
        try:
            countdown_timer(15)
            print("Validando:" + row['codigo'], row['nombre']+ "- primer intento")
            convert(ruta_ws + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".docx", ruta_ws + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".pdf")
            print("Documento para la aplicacion:" + row['codigo'], row['nombre']+ " ok")
        except:
            try:
                print("...fallo...")
                countdown_timer(15)
                print("Validando:" + row['codigo'], row['nombre']+ "- segundo intento")
                convert(ruta_ws + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".docx", ruta_ws + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".pdf")
                print("Documento para la aplicacion:" + row['codigo'], row['nombre']+ " ok")
            except:
                print("error en la generacion del documento "+row['codigo'], row['nombre'])
                traceback.print_exc()
                app = row['codigo'] + " - " +row['nombre']
                total_fallos.append(app)
    
    # Creacion de PDF con codigo HT ---------------------------------------------------------------------------------------------------------------------------------------------
    exit()
    for index, row in dataapp_ht.iterrows():
        try:
            convert(ruta_ht + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".docx", ruta_ht + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".pdf")
           
            print("Documento para la aplicacion:" + row['codigo'], row['nombre']+ " ok")
        except:
            print("error en la generacion del documento "+row['codigo'], row['nombre'])
            traceback.print_exc()
    

    # Creacion de PDF con codigo SI ---------------------------------------------------------------------------------------------------------------------------------------------
    for index, row in dataapp_si.iterrows():
        try:
            convert(ruta_si + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".docx", ruta_si + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".pdf")
            
            print("Documento para la aplicacion:" + row['codigo'], row['nombre']+ " ok")
        except:
            print("error en la generacion del documento "+row['codigo'], row['nombre'])
            traceback.print_exc()

    # Creacion de PDF ubicados en protocolo PAP ---------------------------------------------------------------------------------------------------------------------------------------------
    for index, row in dataapp_pap.iterrows():
        try:
            convert(ruta_pap + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".docx", ruta_pap + row['codigo'] + " - " + row["nombre"] + "/08. Arquitectura app/GTI-F-XXX Formato arquitectura de servidores y red aplicación_"+ row['codigo'] + "_" + row["nombre"] + ".pdf")
            
            print("Documento para la aplicacion:" + row['codigo'], row['nombre']+ " ok")
        except:
            print("error en la generacion del documento "+row['codigo'], row['nombre'])
            traceback.print_exc()

except:
    print("Ocurrio un error:")
    traceback.print_exc()
    print("La conversion fallo para las siguientes aplicaciones:")
    print(total_fallos)
else:
    print("Todas los documentos fueron generados safisfactoriamente")
finally:
    print("ejecucion temrminada...")
    print("Presione cualquier letra para salir")
    k = readchar.readchar()

