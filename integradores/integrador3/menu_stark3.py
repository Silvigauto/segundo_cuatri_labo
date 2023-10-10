from integrador3 import *
from os import system
system('cls')

'''
6. Crear funciones para el manejo del menú principal (usar de guía el anterior desafío)
El menú principal debe tener las siguientes opciones
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Imprimir la lista de nombres y el código del mismo
    3 - Normalizar datos
    4 - Imprimir índice de nombres 
    5 - Navegar fichas 
    6 - Salir

'''

def stark_marvel_app(lista:list):
    while True:
        opcion = stark_menu_principal()
        while opcion == False:
            print('error, ingrese una opción válida')
            opcion = stark_menu_principal()
        
        match opcion:
            case 1:
                stark_imprimir_nombres_con_iniciales1(lista)
            case 2:
                stark_generar_codigos_heroes(lista)
            case 3:
                stark_normalizar_datos(lista)
            case 4:
                stark_imprimir_indice_nombre(lista)
            case 5:
                stark_navegar_fichas(lista)
            case 6:
                break
            case _:
                print('esa opcion no esta dentro del menú')
        
        
    print('Has salido del menú principal')

stark_marvel_app(lista_personajes)