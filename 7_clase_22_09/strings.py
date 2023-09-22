#inicializacion


# #strip  --> rstrip, lstrip-----------------
# mi_cadena = "   esto es una cadena  "
# print(f'aca empieza:{mi_cadena}:aca termina')

# #sin_espacios = mi_cadena.strip()
# sin_espacios = mi_cadena.lstrip()
# print(f'aca empieza:{sin_espacios}:aca termina')



# #upper/lower-------------
# mi_cadena = 'esto es una cadena'
# mayusculas = mi_cadena.upper()
# print(mayusculas)

# #capitalize --> solo la primer letra------------
# mi_cadena = 'esto es una cadena'

# #title --> la primer letra de cada palabra----------
# mi_cadena = 'estoy probando'

# #replace---------------------
# mi_cadena = mi_cadena.replace('probando', '**')
# print(mi_cadena)

# mi_cadena = 'mario,gio,fausto,mariano,german'
# #lista_split = mi_cadena.split(',', 3) --> el 3 parametro opcional que determina cuantas veces hacer el corte 
# lista_split = mi_cadena.split(',')
# for nombre in lista_split:
#     if nombre != 'mariano':
#         print(nombre)


# #join-----------------
# dia = '20'
# mes = '10'
# año = '1987'
# separador = '/'

# fecha = separador.join([dia,mes,año])
# print(fecha)


#zfil---------
# legajo = '555'
# legajo = legajo.zfill(6) #--> cuantos caracteres tiene la cadena, completa

# print(legajo)

#---------------isdigit() / isalnum() --> si una cadena esta compuesta de solo digitos o de solo digitos y caracteres --> devuelve True o False
# mi_cadena = 'hola'
# mi_cadena = mi_cadena.isalnum()
# print(mi_cadena)


#count---------------------------
# mi_cadena = '123pepe'
# print(mi_cadena.count('pe'))

#find-------------
cadena = 'hola hola hola chau hola'
print(cadena.find('hola')) #--> retorna el indice donde empieza la cadena
#print(cadena.find('hola',6)) #el 6.: desde que indice empieza
#print(cadena.rfind(('hola')) #--> empieza desde la derecha