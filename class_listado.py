from db_conn import ConexionDB


class listadoLenceria:

    def __init__(self,desde,hasta):
        self.__cod = ''
        self.__material = ''
        self.__cantidad = ''
        self.__desde = desde 
        self.__hasta = hasta
        self.db = ConexionDB()

    def listado(self):
        query = "SELECT MATERIAL_LENCERIA.NOMBRE,SUM(UNIDADES) AS UNIDADES \
                FROM ENTREGA_LENCERIA, MATERIAL_LENCERIA \
                WHERE ENTREGA_LENCERIA.MATERIAL=MATERIAL_LENCERIA.COD AND FECHA BETWEEN ? AND ? \
                GROUP BY MATERIAL_LENCERIA.NOMBRE"
        valores = (self.__desde, self.__hasta)
        return self.db.ejecutar(query,valores)


