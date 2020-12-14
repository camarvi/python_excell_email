import time

from datetime import datetime


def cadena_busqueda():

    date = datetime.now()
    month = int(date.strftime('%m'))
    year = int(date.strftime('%Y'))

    print ("Mes Actual : %s"  % month)
    print ("Año Actual : %s"  % year)

    if (month ==1):
        desdemonth = 12
        desdeyear = year-1
    else :
        desdemonth = month-1
        desdeyear = year
    
    hastamonth = month
    hastayear = year

    cadena_filtro_desde = str(desdeyear) + '-' + str(desdemonth) + '-01 00:00:00.000'
    cadena_filtro_hasta = str(hastayear) + '-' + str(hastamonth) + '-01 00:00:00.000'

    cadena_desde = '01/' + str(desdemonth) + '/' + str(desdeyear)
    cadena_hasta = '01/' + str(hastamonth) + '/' + str(hastayear)

    print ("Cadena busqueda DESDE : " + cadena_filtro_desde)
    print ("Cadena busqueda HASTA : " + cadena_filtro_hasta)

    return cadena_filtro_desde,cadena_filtro_hasta, cadena_desde , cadena_hasta