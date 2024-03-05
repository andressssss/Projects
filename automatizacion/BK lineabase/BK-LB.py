import traceback
import readchar
import shutil
from datetime import date
from datetime import datetime, timedelta
import os

ruta_docs = ("C:/Users/Usuario/Servicio Nacional de Aprendizaje/TELEFONICA - Infraestructura Centralizada/Data center/Entregables/Otros Entregables/Línea Base Datacenter/")
fecha = date.today()
fecha = fecha.strftime('%d-%m-%Y')
meses = timedelta(days=60)
fechaelim = date.today()-meses

try:
    shutil.copy(ruta_docs + "SENA lineabase -contrato intermedio.xlsx", ruta_docs+"Historico/"+fecha +"SENA lineabase -contrato intermedio.xlsx")
    print("Copia OK")
    historial = os.listdir(ruta_docs+"Historico")
    
    for x in historial:
        fechabk = x[0:10]
        fechaftbk = datetime.strptime(fechabk, '%d-%m-%Y')

        if fechaftbk.date()  < fechaelim:
            print("Documento eliminado:"+x+", Debido a que supera los 60 días de retencion")
            os.remove(ruta_docs+"Historico/"+x)
            
except:
    print("Ocurrio un error:")
    traceback.print_exc()
    print("Presione cualquier letra para salir")
    k = readchar.readchar()
