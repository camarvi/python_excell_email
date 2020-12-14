from openpyxl import Workbook
from openpyxl.styles import Font


def crearFichero(listado_obtenido,desde,hasta):
    #print ("Llamando a un modulo")
    book = Workbook()
    sheet = book.active

    titulo = "LISTADO LENCERIA DEL {} HASTA EL {}".format(desde,hasta)
    #c = "Un texto '{}' y un número '{}'".format(v,n)
    sheet.merge_cells('B1:E1')
    sheet['B1']=titulo
    sheet['B1'].font = Font(color='000000',bold=True, size=14)

    sheet['B3']='ARTICULO'
    sheet['C3']='CANTIDAD'
    sheet['B3'].font = Font(color='58ab28',bold=True, size=12, italic=True)
    sheet['C3'].font = Font(color='58ab28',bold=True, size=12, italic=True)
    posicion=4

    for i in range(0,len(listado_obtenido)):
        elemento= listado_obtenido[i]
        sheet[f'B{posicion}'] = elemento[0]
        sheet[f'C{posicion}'] = elemento[1]
        posicion=posicion+1

    book.save('lenceria.xlsx')