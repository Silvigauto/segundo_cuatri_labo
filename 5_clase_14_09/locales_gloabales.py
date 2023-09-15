from os import system
system('cls')

def estableces_valor_local(valor):
    print(f'valor de la variable dentro de la funcion {valor}')
    print(f'id de la variable dentro de la funcion {id(valor)}')


mi_variable = 55
estableces_valor_local(mi_variable)
print(f'valor de la variable fuera de la funcion {mi_variable}')
print(f'valor de la variable fuera de la funcion {id(mi_variable)}')
