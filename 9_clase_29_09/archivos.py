import os
#crear un archivo
'''
archivo = open('9_clase_29_09\holaa.txt', 'w')
archivo.write('hola1bd')
archivo.close

lectura--> para leer un archivo siempre tiene que existir primero, sino tira error
archivo = open('hola.txt', 'r')
informacion_archivo = archivo.read()
print(informacion_archivo)
archivo.close()#--> siempre hay que cerrar el archivo
'''

#leer un archivo
'''
#para chequear que el archivo exista
if os.path.exists('9_clase_29_09\holaa.txt'):
    archivo = open('9_clase_29_09\holaa.txt', 'r',encoding = "utf-8")
    informacion_archivo = archivo.read()
    print(informacion_archivo)
    print(archivo.close) #--> retorna False, xq todavia no se cerro el archivo
    archivo.close()#--> siempre hay que cerrar el archivo
else:
    print('error')
'''

#leer cada linea del archivo con readlines() --> y crea una lista
'''
#1.abro el archivo
archivo = open('9_clase_29_09\holaa.txt', 'r')
if os.path.exists('9_clase_29_09\holaa.txt'):
    #2.manipulamos el archivo
    for linea in archivo.readlines(): #--> hace que podamos recorrer todas las lineas del archivos y devuelve una lista
        print(linea, end ="") #end ="" --> para evitar que haga doble salto de linea, porque por default ya hay un \n
    
    #3.cerramos el archivo
    archivo.close()
'''

#recorrer el objeto file que es un iterable --> no lo agrega a una lista por lo tanto no consume tantos recursos(para archivos muy grandes hace la diferencia)
'''
#1.abro el archivo
archivo = open('9_clase_29_09\holaa.txt', 'r')
if os.path.exists('9_clase_29_09\holaa.txt'):
    #2.manipulamos el archivo
    for linea in archivo: #--> hace que podamos recorrer todas las lineas del archivos y devuelve una lista
        print(linea, end ="") #end ="" --> para evitar que haga doble salto de linea, porque por default ya hay un \n el print ya hace un \n
    
    #3.cerramos el archivo
    archivo.close()
'''
#readline() --> solo abre la primera linea
'''
#1.abro el archivo
archivo = open('9_clase_29_09\holaa.txt', 'r')
if os.path.exists('9_clase_29_09\holaa.txt'):
    #2.manipulamos el archivo
    primer_linea = archivo.readline()  #--> solo la primera linea
    primer_linea = archivo.readline() #--> si lo vuelvo a ejecutar lee una sola linea pero a partir del puntero anterior
    print(primer_linea)
    #3.cerramos el archivo
    archivo.close()
'''

#writelines --> si no existe el arhivo, lo crea, si existe lo sobreescribe
'''
archivo = open('9_clase_29_09\holaa.txt', 'w')
lineas_texto = ['Primer linea de texto\n',
            'segunda linea\n',
            'tercera linea\n']
archivo.writelines(lineas_texto)
archivo.close()
'''

#with -->administrador de contexto, python se encarga de cerrarlo solo
'''
if os.path.exists('9_clase_29_09\holaa.txt'):
    with open('9_clase_29_09\holaa.txt', 'r+') as archivo:
        for linea in archivo:
            print(linea, end="")
        #estoy en el with
        print(archivo.closed) #false
    #fuera del with
    print(archivo.closed) #true
else:
    print('error')
'''

#append--> si no existe lo crea
with open('onmbre.txt', 'a') as archivo: 
    archivo.write('hola a todos') #cada vez que se ejecuta se vuelve a escribir al final(se situa en el ultima byte) \n para q no se escriba uno al lado del otro