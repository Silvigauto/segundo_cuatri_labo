from os import system
system('cls')


from data_stark import *

while True:
    respuesta = int(input("1.Imprimir datos superheroes\n2.Identidad y peso del superheroe con mayor fuerza\n3. Nombre e identidad del superheroe mas bajo\n4.Peso promedio de los superheroes masculinos\n5.Superheroes que superen el promedio de fuerza femenino\n6.Salir\nElija una opcion:"))
    match respuesta:
        case 1:
            #A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
            for heroe in lista_personajes:
                nombre = heroe['nombre']
                identidad = heroe['identidad']
                empresa = heroe['empresa']
                altura = float(heroe['altura'])
                peso = float(heroe['peso'])
                genero = heroe['genero']
                color_ojos = heroe['color_ojos']
                color_pelo = heroe['color_pelo']
                fuerza = int(heroe['fuerza'])
                inteligencia = heroe['inteligencia']

                print(f'{nombre:20}{identidad:30}{empresa:15}{altura}/{peso}/{genero}/{color_ojos}/{color_pelo}/{fuerza}/{inteligencia}')                       
        case 2:
            #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
            bandera_primero = True
            for heroe in lista_personajes:
                fuerza = float(heroe['fuerza'])
                if bandera_primero == True or fuerza > maxima_fuerza:
                    maxima_fuerza = fuerza
                    bandera_primero = False

            print(f'Maxima fuerza: {maxima_fuerza}')
            for heroe in lista_personajes:
                fuerza = int(heroe['fuerza'])
                if fuerza == maxima_fuerza:
                    nombre = heroe['nombre']
                    identidad = heroe['identidad']
                    peso = heroe['peso']
                    print(f'{nombre} - {identidad} - {peso}')
        case 3:
            #C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
            bandera_primero = True
            for heroe in lista_personajes:
                altura = float(heroe['altura'])
                if bandera_primero == True or altura < altura_minima:
                    altura_minima = altura
                    bandera_primero = False

            print(f'La altura minima es {altura_minima}')
            for heroe in lista_personajes:
                altura = float(heroe['altura'])
                nombre = heroe['nombre']
                identidad = heroe['identidad']
                if altura == altura_minima:
                    print(f'{nombre} - {identidad}')
        case 4:
            #D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
            acumulador_peso_masculino = 0
            contador_masculinos = 0
            for heroe in lista_personajes:
                genero = heroe['genero']
                if genero == 'M':
                    peso = float(heroe['peso'])
                    acumulador_peso_masculino += peso
                    contador_masculinos += 1

            promedio_peso_masculino = acumulador_peso_masculino/contador_masculinos
            print(f'El peso promedio de los masculinos es {promedio_peso_masculino}')
        case 5:
            #E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
            # género) los cuales su fuerza supere a la fuerza promedio de todas las
            # superhéroes de género femenino

            acumulador_fuerza_femenino = 0
            contador_fuerza_femenino = 0

            for heroe in lista_personajes:
                genero = heroe['genero']
                if genero == 'F':
                    fuerza = float(heroe['fuerza'])
                    acumulador_fuerza_femenino += fuerza
                    contador_fuerza_femenino += 1

            promedio_fuerza_femenino = acumulador_fuerza_femenino / contador_fuerza_femenino
            print(f'El promedio de fuerza femenino es {promedio_fuerza_femenino}')
            for heroe in lista_personajes:
                fuerza = float(heroe['fuerza'])
                if fuerza > promedio_fuerza_femenino:
                    nombre = heroe['nombre']
                    peso = float(heroe['peso'])
                    print(f'{nombre} - {peso}')
        case 6:
            break






