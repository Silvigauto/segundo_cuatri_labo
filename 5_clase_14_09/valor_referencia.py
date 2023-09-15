#todo se pasa por referencia, la unica forma de cambiarlo es con un return y atajarlo

#INMUTABLE
def modificar_valor(x):
    x = x + 10
    return x
numero = 5
numero = modificar_valor(numero)
print(numero)

#MUTABLE
def cargar_lista(lista):
    lista.append(45)

mi_lista = [4,9,8,44,3]

cargar_lista(mi_lista)
print(mi_lista)