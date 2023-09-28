
from os import system
system('cls')

from data import * 

import re
from datetime import datetime

#########TITULOS#################
lista_coincidencias = []
'''

'QUEVEDO || BZRP Music Sessions #52'
'L-Gante || BZRP Music Sessions #38'
['L', 'Gante ', ' BZRP Music Sessions ', '38']
'title': 'Jeeiph - Tetrix (Bizarrap Remix)'
'ACZINO ', ' BZRP Freestyle Sessions ', '8'
'title': 'Bizarrap, Trueno, Acru - Jugador del Año'

'''

def regex_titulo(titulo:str):
    lista = re.split("\|\||#|-", titulo)
    #print(lista)

    #imprimo solo las freestyle sessions---------
    if len(lista) >= 2 and lista[1] == ' BZRP Freestyle Sessions ':
        print(lista)
        lista_coincidencias.append(lista)

    #imprimo las BZRP Music Sessions-------
    if len(lista) >= 3 and (lista[1].strip() == 'BZRP Music Sessions' or lista[2].strip() == 'BZRP Music Sessions') :
        lista_coincidencias.append(lista)
        print(f"{lista[0]:20} - {lista[2]} ")

    #imprimo las que estan separadas por guion -----
    if len(lista) == 2:
        print(f"{lista[0]:20} - {lista[1]}")
        lista_coincidencias.append(lista)

# for tema in lista_bzrp:
#     regex_titulo(tema["title"])


#print(len(lista_coincidencias)) #74

#print(len(lista_bzrp))#78

#############FECHAS####################
'''
'date': '2022-07-06 00:00:00'
'''
def regex_fecha(fecha:str):
    fecha_formato = re.split('-|:| ', fecha)
    año = fecha_formato[0]
    mes = fecha_formato[1]
    dia = fecha_formato[2]
    print(f'{año}/{mes}/{dia}')

for tema in lista_bzrp:
    regex_fecha(tema["date"])