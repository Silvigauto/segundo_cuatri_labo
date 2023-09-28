#Silvina Gauto - 1B - Integrador 2 

from funciones import *

def stark_marvel_app(lista:list):
    bandera_opciones = False

    #primero hago que el usuario elija la opcion uno, hasta que no haga eso no se termina el bucle y no puede pasar el siguiente
    while bandera_opciones == False:

        #pido la opcion y mientras no sea validada no dejo que salga del bucle
        opcion = stark_menu_principal()
        while opcion == False:
            print('elija una opcion correcta')
            opcion = stark_menu_principal()
        
        if opcion == 1:
            datos_normalizados = stark_normalizar_datos(lista)
            if datos_normalizados:
                print('Datos normalizados')
                bandera_opciones = True
            else:
                print('Hubo un error al normalizar los datos. Verifique que la lista no esté vacía o que los datos ya no se hayan normalizado anteriormente')
        #si el usuario quiere salir del menu directamente
        elif opcion == 12:
            break
        elif opcion > 12:
            print('esa opción no esta dentro del menú')
        else:
            print('debe normalizar los datos primero')

    #recien cuando bandera_opciones este en true puede salir del bucle y entrar al bucle gral de opciones
    while True:

        #analizo primero si el usuario quere salir del menu asi no sigo mostrando las opciones
        if opcion == 12:
            break

        #pido la opcion y mientras no sea validada no dejo que salga del bucle
        opcion = stark_menu_principal()
        while opcion == False:
            print('elija una opcion correcta')
            opcion = stark_menu_principal()

        match opcion:
            case 1:
                datos_normalizados = stark_normalizar_datos(lista)
                if datos_normalizados == False:
                    print('ya se ha normalizado la lista anteriormente')
            case 2:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                for heroe in lista_no_binarios:
                        print(obtener_nombre_y_dato(heroe, 'genero'))
            case 3:
                imprimir_heroes_mas_altos_genero(lista, 'F', 'altura')
            case 4:
                imprimir_heroes_mas_altos_genero(lista, 'M', 'altura')
            case 5:
                imprimir_heroes_mas_debiles_genero(lista, 'M', 'fuerza')
            case 6:
                imprimir_heroes_mas_debiles_genero(lista, 'NB', 'fuerza')
            case 7:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                print(mostrar_promedio_dato(lista_no_binarios, 'fuerza'))
            case 8:
                contar_superheroes_por_categoria(lista, 'color_ojos')
            case 9:
                contar_superheroes_por_categoria(lista, 'color_pelo')
            case 10:
                listar_superheroes_por_categoria(lista, 'color_ojos')
            case 11:
                listar_superheroes_por_categoria(lista, 'inteligencia')
            case 12:
                break
            case _:
                print('esa opción no esta dentro del menú')








