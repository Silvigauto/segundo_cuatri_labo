#tipos de funciones
# def sumar(): #definiendo
#     primer_numero = int(input('ingrese el primer numero: '))
#     segundo_numero = int(input('ingrese el segundo numero: '))
    
#     suma = primer_numero + segundo_numero

#     print(f'La suma es: {suma}')

#sumar()#invocando

# def sumar(un_numero, otro_numero):
#     suma = un_numero + otro_numero
#     print(f'La suma es: {suma}')

# primer_numero = 7
# segundo_numero = 5

#sumar(primer_numero, segundo_numero)

# def sumar():
#     primer_numero = int(input('ingrese el primer numero: '))
#     segundo_numero = int(input('ingrese el segundo numero: '))

#     suma = primer_numero + segundo_numero
#     return suma 

# resultado = sumar()
# print(f"el resultado es {resultado}")

import random

def sumar(un_numero, otro_numero):
    suma = un_numero + otro_numero
    return suma

primer_numero = random.randint(1,60)
segundo_numero = random.randint(55,236)

resultado =  sumar(primer_numero, segundo_numero)

total = resultado * 0.8

print(f'el total: {total}')