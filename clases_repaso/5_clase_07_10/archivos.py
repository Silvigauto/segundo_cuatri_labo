import re
from os import system
system('cls')
'''
Traer datos desde archivo: guardará el contenido del archivo
pokemones.csv en una colección. Tener en cuenta que tanto tipos y
habilidades deben estar guardadas en algún tipo de colección, debido a que
un pokemón puede tener más de un tipo y más de una habilidad.
'''


#N° Pokedex,Nombre,Tipo,Poder de Ataque,Poder de Defensa,Habilidades
def parsear(path:str)->list:
    lista_pokemones = []
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            registro = re.split(",|\n", linea)
            pokemon = {}
            pokemon['numero'] = registro[0]
            pokemon['nombre'] = registro[1]
            pokemon['tipo'] = re.split('/', registro[2])
            pokemon['poder_ataque'] = registro[3]
            pokemon['poder_defensa'] = registro[4]
            pokemon['habilidades'] = re.split('\|\*\|', registro[5])
            lista_pokemones.append(pokemon)
    return lista_pokemones


lista_pokemones = parsear("Pokemones.csv")



'''
2. Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
pokemones que corresponden a ese tipo.
'''

def setear_lista_tipos(lista):
    lista_tipos = []
    for pokemon in lista:
        for tipo in pokemon['tipo']:
            lista_tipos.append(tipo)
    lista_tipos = set(lista_tipos)
    return lista_tipos

def listar_cantidad_por_tipo(lista):
    lista_tipos = setear_lista_tipos(lista)
    for tipo in lista_tipos:
        contador = 0
        for pokemon in lista:
            for elemento in pokemon['tipo']:
                if elemento == tipo:
                    contador += 1
        print(f'{tipo}: {contador}')

'''
3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
de ataque de cada pokemon que corresponde a ese tipo.
'''

