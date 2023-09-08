'''
Ejercicio 02
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:
A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)
B) Luego del ingreso mostrar en pantalla todos los datos.
C) Realizar los siguientes informes:
1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.

'''
from os import system
system('cls')


'''
# Lista de 20 nombres
lista_nombres = ["Ana", "Juan", "María", "Carlos", "Laura", "Pedro", "Sofia", "Andrés", "Valentina", "Luis", "Marta", 
                "Alejandro", "Isabel", "Sergio", "Gabriela", "Daniel", "Camila", "Esteban", "Natalia", "Francisco"]

# Lista de 20 números no menores a 10,000
lista_montos = [10000, 12345, 15678, 20000, 25432, 30000, 35678, 40000, 45678, 50000, 55432, 
                60000, 65789, 70000, 75432, 80000, 85678, 90000, 95432, 100000]

# Lista de cantidad de instrumentos utilizados
lista_instrumentos = [50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290, 60, 80, 100, 120, 140, 160, 180]


# Lista de 20 tipos: CEDEAR, BONOS, MEP
lista_tipos = ["CEDEAR", "BONOS", "MEP", "BONOS", "CEDEAR", "MEP", "CEDEAR", "BONOS", "MEP", 
                "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "CEDEAR", "BONOS"]
'''

lista_nombres = []
lista_montos = []
lista_instrumentos = []
lista_tipos = []


respuesta = 'si'

while respuesta == 'si':
    nombre = input('ingrese nombre')
    while nombre == '':
        nombre = input('ingrese nombre')
    lista_nombres.append(nombre)

    monto = int(input('Ingrese monto'))
    while monto < 10000:
        monto = int(input('Ingrese monto'))
    lista_montos.append(monto)

    cantidad_instrumentos = int(input('Ingrese cantidad de instrumentos'))
    while cantidad_instrumentos < 1:
        cantidad_instrumentos = int(input('Ingrese cantidad de instrumentos'))
    lista_instrumentos.append(cantidad_instrumentos)

    tipo = input('Ingrese el tipo: CEDEAR - MEP - BONOS')
    while tipo != 'CEDEAR' and tipo != 'MEP' and tipo != 'BONOS':
        tipo = input('Ingrese el tipo: CEDEAR - MEP - BONOS')
    lista_tipos.append(tipo)

    respuesta = input('Desea continuar? si o no')
    if respuesta == 'no':
        break


bandera_instrumento = True
bandera_menos_dinero_invertido = True
contador_usuarios = 0

contador_cedear = 0
acumulador_monto  = 0

contador_mep  = 0

acumulador_cedear = 0
acumulador_mep = 0
acumulador_bonos = 0

# {ııııA╚╚}{þ{}}§☻☺♥♦♣♠•◘○8AA-♀[[↨8→→→→→♥►↨▬-☼♀]]
if len(lista_nombres) > 0:
    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        monto = lista_montos[i]
        cantidad_instrumentos = lista_instrumentos[i]
        tipo = lista_tipos[i]

        print(f"{nombre:15} {monto}\t{cantidad_instrumentos:15} \t{tipo}")

        #1 Tipo de instrumento que más se operó.
        match tipo:
            case 'MEP':
                acumulador_mep += cantidad_instrumentos
            case 'BONOS':
                acumulador_bonos += cantidad_instrumentos
            case 'CEDEAR':
                acumulador_cedear += cantidad_instrumentos


        #2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
        if cantidad_instrumentos >= 150 and cantidad_instrumentos <= 200 and monto > 50000:
            contador_usuarios += 1

        #3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.
        if tipo == 'MEP' or tipo == 'BONOS':
            if bandera_menos_dinero_invertido == True or monto < monto_menos_invertido:
                monto_menos_invertido = monto
                bandera_menos_dinero_invertido = False

        #4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio
        acumulador_monto += monto

        #5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
        if tipo != 'MEP' and monto <= 50000:
            contador_mep += 1

else:
    print('la lista esta vacia')

#1 Tipo de instrumento que más se operó.
if acumulador_mep > acumulador_cedear and acumulador_mep >acumulador_bonos:
    acumulador_maximo = 'acumulador mep'
else:
    if acumulador_bonos> acumulador_cedear:
        acumulador_maximo =  'acumulador bonos'
    else:
        acumulador_maximo = 'acumulador cedear'

print(f'El acumulador maximo es: {acumulador_maximo}')

#2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
print(f'Cantidad de usuarios que compraron entre 150 y 200 bonos y que inviertieron mas de $50000 es: {contador_usuarios}')

#3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.
for i in range(len(lista_nombres)):
    nombre = lista_nombres[i]
    monto = lista_montos[i]
    cantidad_instrumentos = lista_instrumentos[i]
    tipo = lista_tipos[i]

    if bandera_menos_dinero_invertido == False:
        if monto == monto_menos_invertido and (tipo == 'MEP' or tipo == 'BONOS'):
            print(f'Nombre: {nombre} - Cantidad de instrumentos: {cantidad_instrumentos}')
    else:
        print('No se ha ingresado BONOS o MEP')

#4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio
promedio_monto = acumulador_monto / len(lista_montos)
#encuentro coincidencias
for i in range(len(lista_nombres)):
    nombre = lista_nombres[i]
    monto = lista_montos[i]
    cantidad_instrumentos = lista_instrumentos[i]
    tipo = lista_tipos[i]

    if tipo == 'CEDEAR' and monto > promedio_monto:
        print(f'Nombre usuario que inviertio en cedear y su inversion supera el monto promedio: {nombre}')


#5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
porcentaje_usuarios_mep = (contador_mep*100)/len(lista_montos)
print(f'Porcentaje de usuarios que no invirtieron en MEP, cuyo monto no supera los $50000: {porcentaje_usuarios_mep}%')

