#Silvina Gauto - 1B - Integrador 2 

from os import system
system('cls')
from data_stark import * 
from funciones import *

stark_marvel_app(lista_personajes)








































# bandera_opciones = False
# while True:
#     imprimir_menu()
#     opcion = int(input('ingrese una opcion'))

#     match opcion:
#         case 1:
#             datos_normalizados = stark_normalizar_datos(lista_personajes)
#             if datos_normalizados:
#                 print('datos normalizados')
#                 bandera_opciones = True
#             else:
#                 print('Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente')
#         case 2:
#             if bandera_opciones:
#                 obtener_maximo(lista_personajes, 'fuerza')
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 3:
#             if bandera_opciones:
#                 print(obtener_minimo(lista_personajes, 'altura'))
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 4:
#             if bandera_opciones:
#                 mayor_dato = obtener_maximo(lista_personajes, 'peso')
#                 menor_dato = obtener_minimo(lista_personajes, 'peso')
#                 print(obtener_dato_cantidad(lista_personajes, mayor_dato, 'peso'))
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 5:
#             if bandera_opciones:
#                 pass
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 6:
#             if bandera_opciones:
#                 mas_pesado = obtener_maximo(lista_personajes,'peso')
#                 lista_mas_pesados = obtener_dato_cantidad(lista_personajes,mas_pesado ,'peso')
#                 stark_imprimir_heroes(lista_mas_pesados) # Imprimo sólo los héroes más pesados
#                 #stark_imprimir_heroes(lista_personajes) # Imprimo todos los héroes
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 7:
#             if bandera_opciones:
#                 print(sumar_dato_heroe(lista_personajes, 'altura'))
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 8:
#             if bandera_opciones:
#                 print(validar_entero('456b'))
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 9:
#             if bandera_opciones:
#                 #print(calcular_promedio(lista_personajes, 'peso'))
#                 print(mostrar_promedio_dato(lista_personajes, 'peso'))
#             else:
#                 print('debe normalizar los datos primero, elija la opcion uno')
#         case 10:
#             break

# print('Has salido del menú')