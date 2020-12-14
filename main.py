import pyodbc
from datetime import datetime

from maneja_excell import crearFichero
from fechas import  cadena_busqueda
from email_con_adjunto import enviar_email
from class_listado import listadoLenceria


direccion_servidor = '10.xxxxxx'
nombre_bd = 'MIDB'
nombre_usuario = 'usuario'
password = 'xxxxxxxx'


def obtenerListado(desde,hasta,cadena_desde,cadena_hasta):
    l_listado = listadoLenceria(desde,hasta)
    listado_obtenido =  l_listado.listado()
    #print(listado_obtenido)
    crearFichero(listado_obtenido,cadena_desde,cadena_hasta)
    


def main():
    try:
        conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
        print("Conectado a BD")
        desde, hasta, cadena_desde , cadena_hasta = cadena_busqueda()
        obtenerListado(desde,hasta,cadena_desde,cadena_hasta)
        print ("DESDE : " + cadena_desde)
        print ("HASTA : " + cadena_hasta)
        enviar_email()
    except Exception as e:
    # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)



if __name__ == "__main__":
    main()