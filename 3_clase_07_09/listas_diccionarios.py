from os import system
system('cls')

#LISTAS
lista = [1,2,3,5,7,9,4]

#SLICE  
lista[0:3] #0--> inclusivo 3--> excluyente  [1, 2, 3]

#INSERT --> para agregar en una posicion de la lista
lista.insert(1,100)

#EXTEND --> recibe una lista y la agrega al final
lista_4 = [7,4,1,33]
lista.extend(lista_4)

#REMOVE --> elimina un elemento de la lista, solo la primera ocurrencia
lista.remove(4)

#PARA CAMBIAR UN VALOR POR SU INDICE --> reemplazar
lista[2] = 10000


#TUPLAS --> inmutable
tupla = (2,5,6)
tupla.count(5) #--> cuantas ocurrencias del 5 hay

#SETS --> devuelve un iterable set(nuevo), que luego puedo convertir a lista, elimina repeticiones y genera un orden distinto
lista = [1,9,2,3,3,4,5,4,7,9,4]
mi_set = list(set(lista))

#DICCIONARIOS

# un_empleado = {}
# un_empleado['nombre'] = 'Juan'
# un_empleado['sueldo'] = 50000.25
# un_empleado['edad'] = 35

# for clave in un_empleado:
#     print(clave) #nombre sueldo edad -->itero las claves

# for clave in un_empleado:
#     print(un_empleado[clave]) #Juan 50000.25 35

# primer_empleado = {'nombre': 'Juan', 'sueldo': 50000.25, 'edad':35}
# segundo_empleado = {'nombre': 'Maria', 'sueldo': 90000.85, 'edad':28}
# tercer_empleado = {'nombre': 'Luis', 'sueldo': 45000.77, 'edad':30}

# lista_empleados = [primer_empleado, segundo_empleado, tercer_empleado]

lista_empleados = []

for i in range(3):
    nombre = input('Ingrese nombre')
    sueldo = float(input('ingrese sueldo'))
    edad = int(input('ingrese edad'))
    un_empleado = {}
    un_empleado['nombre'] = nombre
    un_empleado['sueldo'] = sueldo
    un_empleado['edad'] = edad
    lista_empleados.append(un_empleado)





for empleado in lista_empleados:
    nombre = empleado['nombre']
    sueldo = empleado['sueldo']
    edad = empleado['edad']
    print(f"{nombre:10}{sueldo:10}{edad:10}")
