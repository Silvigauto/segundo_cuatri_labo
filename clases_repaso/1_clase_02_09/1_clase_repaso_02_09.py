#EJERCICIO 1 CLASE REPASO
from os import system
system('cls')

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertir
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donnuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

El programa tendra precargado un menú de opciones en el que debemos programar lo siguiente

1.Cargar voto, está opción agregara a las listas un voto en especifico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    genero (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)   
    
2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
3-Género que predomina en la empresa.
4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre 
entre los 18 y 30.
5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
6-Salir
'''

lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
            "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]

lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
            32, 22, 29, 27, 19, 49, 27, 22, 29, 27]

lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", 
                "Otro", "Masculino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", 
                "Femenino", "Masculino", "Femenino"]

lista_votos = ["APPLE", "DUNKIN", "IKEA", "APPLE", "TACO", "DUNKIN", "TACO", "APPLE", "TACO", "APPLE",
            "IKEA", "APPLE", "DUNKIN", "DUNKIN", "APPLE", "IKEA", "APPLE", "DUNKIN", "IKEA", "TACO"]    

'''
for i in range(len(lista_edades)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    voto = lista_votos[i]

    print(f'{nombre:10}{edad:10}\t {genero:10}\t {voto:10}')
'''





while True:

    print("\n1-Cargar Voto\n2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años\n3-Género que predomina en la empresa.\n4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino o su edad se encuentre.\n5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados\n6-Salir")

    opcion = input("Ingrese una opción 1-6:")
    opcion = int(opcion)
    if opcion == 1:
        print("1")
    elif opcion == 2:
        #2-Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
        contador_apple_35 = 0
        for i in range(len(lista_edades)):
            edad = lista_edades[i]
            voto = lista_votos[i]

            if voto == 'APPLE' and edad < 35:
                contador_apple_35 += 1
        print(contador_apple_35)
    elif opcion == 3:
        #3-Género que predomina en la empresa.
        contador_femenino = 0
        contador_masculino = 0
        contador_otro = 0
        for i in range(len(lista_edades)):
            genero = lista_generos[i]
        
            match genero:
                case 'Femenino':
                    contador_femenino += 1
                case 'Masculino':
                    contador_masculino += 1
                case 'Otro':
                    contador_otro += 1

        if contador_femenino > contador_masculino and contador_femenino > contador_otro:
            genero_predominante = f'Femenino: {contador_femenino}'
        elif contador_masculino > contador_otro:
            genero_predominante = f'Masculino: {contador_masculino}'
        else:
            genero_predominante = f'Otro: {contador_otro}'

        print(f'genero predominante --> {genero_predominante}')
    elif opcion == 4:
        #4-Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea 
        # Femenino o su edad se encuentre entre los 18 y 30.

        contador_porcentaje = 0
        for i in range(len(lista_edades)):
            edad = lista_edades[i]
            genero = lista_generos[i]
            voto = lista_votos[i]

            if voto != 'Apple' and (genero != 'Femenino' or (edad >= 18 and edad <= 30)):
                contador_porcentaje += 1
            
        porcentaje = (contador_porcentaje * 100)/len(lista_votos)
        print(porcentaje)
    elif opcion == 5:
        #5-Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la 
        # edad promedio de todos los empleados
        acumulador_edad = 0
        for i in range(len(lista_edades)):
            edad = lista_edades[i]
            acumulador_edad += edad

        promedio_edad = acumulador_edad/len(lista_nombres)

        for i in range(len(lista_edades)):
            nombre = lista_nombres[i]
            edad = lista_edades[i]
            voto = lista_votos[i]
            
            if (voto == 'TACO' or voto == 'IKEA') and edad > promedio_edad:
                print(F'Nombre: {nombre} Edad {edad}')
    elif opcion == 6:
        print("Adios")
        break
    else:
        print("Opcion incorrecta (1-6)")

