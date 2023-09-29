from os import system
system('cls')
import re

#SPLIT--> donde encuentra coincidencia con el regex genera un corte
cadena = 'hola mundo 125c'
cadena2 = 'hola mundo chau'
cadena3 = 'hola mundo 1253 chau '
re.split(" ", cadena) #['Hola', 'mundo', '1c'] --> donde encuentra el espacio, me separa en lista
re.split("[a-z]", cadena ) #['', '', '', '', ' ', '', '', '', '', ' 125', ''] --> donde encuentra un caracter de la a la z(minuscula) hace el corte, en este caso en todo lados menos en el numero
re.split("[a-z ]", cadena )#['', '', '', '', '', '', '', '', '', '', '', '125', ''] --> ahora contempla el espacio
re.split("[a-z ]+", cadena )#['', '125', ''] --> analiza los CONJUNTOS de la a la z
re.split("[0-9]+", cadena )#['hola mundo ', 'c']
re.split("hola|chau| ", cadena2 )#['', '', 'mundo', '', '']
re.split("[a-z]|[0-9]", cadena3 )
re.split("[a-z]|[0-9| ]", cadena3 )

#SEARCH--> devuelve none o un objeto de tipo match que indica la tupla del indice en donde se encontro la regex y donde terminó
re.search(" ", "hola") #None --> devuelve none porque no encontro un espacio en la cadena
re.search(" ", "hola como estan?") #<re.Match object; span=(4, 5), match=' '> -->solo encuentra la primera coincidencia
re.search("como", "hola como estan?")#<re.Match object; span=(5, 9), match='como'>
re.search("[a-z]+", "hola como estan?") #<re.Match object; span=(0, 4), match='hola'>
re.search("[a-z]+", "hola como estan?").span() #me devuelve el span
re.search("[a-z]+", "hola como estan?").start() #donde empieza
re.search("[a-z]+", "hola como estan?").end() #donde termina
re.search("[a-z]+", "hola como estan?").group()#devuelve con que hizo match

#FINDALL
texto = "uno 1 dos 2 tres 3 cuatro"
texto1 = "uno 1 dos 2 tres 3 cuatro 44"
re.findall(" ", texto) #[' ', ' ', ' ', ' ', ' ', ' '] --> me devuelve todos los espacios que encontro
re.findall("[0-9]", texto) #['1', '2', '3']
re.findall("[0-9]+", texto1) #['1', '2', '3', '44']
re.findall("[a-z]+", texto1) #['uno', 'dos', 'tres', 'cuatro']
re.findall("[a-zA-Z]+", "Uno 1 dos 2 tres 3 cuatro 44") #['Uno', 'dos', 'tres', 'cuatro']  -->incluye mayusculas
re.findall("[a-zA-Z]{3}", "Uno 1 dos 2 tres 3 cuatro 44") #['Uno', 'dos', 'tre', 'cua', 'tro'] --> que tengan como minimo 3 caracteres ?? y si quiere como minimo 3 y como maximo indefinido
re.findall("[a-zA-Z]{3,6}", "Uno 1 dos 2 tres 3 cuatro 44") #['Uno', 'dos', 'tres', 'cuatro'] --> minimo y maximo


#SUB --> REEMPLAZA UNA COSA CON OTRA, RECIBE --> QUE QUIERO REEMPLZAR, POR QUÉ LO QUIERO REEMPLAZAR Y EN DONDE REEMPLAZAR
texto = "abc abc ccc ddd abc aaa"
result = re.sub('abc', '', "abc abc ccc ddd abc aaa") #  ccc ddd  aaa
result = re.sub('abc ', '', "abc abc ccc ddd abc aaa")#ccc ddd aaa --> incluye los espacios
result = re.sub('abc', 'xyz', "abc abc ccc ddd abc aaa")#xyz xyz ccc ddd xyz aaa

result = re.sub('\\s+', ' ', "abc abc ccc ddd  abc aaa") #reeemplaza el espacio duplicado \\s: espacio \s:secuencia de escape \\s+:un espacio o mas
result = re.sub(r'\s+', ' ', "abc abc ccc ddd  abc aaa") #al poner r no hace falta usa doble contrabarra
result = re.sub(r'\s+', '*', "abc abc ccc ddd  abc aaa")#abc*abc*ccc*ddd*abc*aaa --> donde haya un espacio o mas reemplaza con *
result = re.sub(r'\s\s', '*', "abc abc ccc ddd    abc aaa")#abc abc ccc ddd**abc aaa --> encontro dos grupos de dos espacios entonces son dos astericos



print(result)