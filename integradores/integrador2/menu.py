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
                for heroe in lista:
                    if heroe['genero'] == 'NB':
                        print(obtener_nombre_y_dato(heroe, 'genero'))
            case 3:
                lista_femeninos = obtener_superheroes_por_genero(lista, 'F')
                maximo = obtener_maximo(lista_femeninos, 'altura')
                lista_coincidencias = obtener_dato_cantidad(lista_femeninos, maximo, 'altura')
                for heroe in lista_coincidencias:
                    print(obtener_nombre_y_dato(heroe, 'altura'))
            case 4:
                lista_masculinos = obtener_superheroes_por_genero(lista, 'M')
                maximo = obtener_maximo(lista_masculinos, 'altura')
                lista_coincidencias = obtener_dato_cantidad(lista_masculinos, maximo, 'altura')
                for heroe in lista_coincidencias:
                    print(obtener_nombre_y_dato(heroe, 'altura'))
            case 5:
                lista_masculinos = obtener_superheroes_por_genero(lista, 'M')
                minimo = obtener_minimo(lista_masculinos, 'fuerza')
                lista_coincidencias = obtener_dato_cantidad(lista_masculinos, minimo, 'fuerza')
                for heroe in lista_coincidencias:
                    print(obtener_nombre_y_dato(heroe, 'fuerza'))
            case 6:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                minimo = obtener_minimo(lista_no_binarios, 'fuerza')
                lista_coincidencias = obtener_dato_cantidad(lista_no_binarios, minimo, 'fuerza')
                for heroe in lista_coincidencias:
                    print(obtener_nombre_y_dato(heroe, 'fuerza'))
            case 7:
                lista_no_binarios = obtener_superheroes_por_genero(lista, 'NB')
                acumulador = sumar_dato_heroe(lista_no_binarios, 'fuerza')
                promedio = dividir(acumulador, len(lista_no_binarios))
                print(f'Promedio: {promedio:0.2f}')
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








