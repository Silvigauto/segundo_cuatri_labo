# a = int(input('ingrese el dividendo: '))
# b = int(input('ingrese el divisor : '))

# c = a/b
# print(c)

# try:
#     a = int(input('ingrese el dividendo: '))
#     b = int(input('ingrese el divisor : '))

#     c = a/b
#     print(c)
# except Exception as ex:
#     if type(ex) is ZeroDivisionError:
#         print('cero')
#     elif type(ex) is TypeError:
#         print('cadena')
#     elif type(ex) is ValueError:
#         print('el dividendo es una cadena')

# lista = [5,6]

# try:
#     a = int(input('ingrese el dividendo: '))
#     b = int(input('ingrese el divisor : '))
#     print(lista[5]) #index error
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print('cero')
# except ValueError:
#     print('cadena')
# except NameError: #por si estas tratando de usar una variable que no exista
#     print('error de asignacion')
# except Exception as ex:
#     print(type(ex))
# # except Exception: #else
# #     print('hubo un error general')

# bandera = True

# while bandera == True:
#     try:
#         a = int(input('ingrese un numero'))
#         bandera = False
#     except ValueError:
#         print('error, reingrese')


# c = a+5
# print(c)

def pedir_entero(mensaje, mensaje_error, intentos,min,max)->int|None:
    retorno = None
    for i in range(intentos):
        valor = input(mensaje)
        try:
            valor = int(valor)
            raise
            retorno = valor
            break #rompo el for
        except ValueError:
            print(mensaje_error)
    
    return retorno

numero = pedir_entero('ingrese nota', 'error al ingresar una nota', 3, 1,10)
if numero != None:
    print(f'el numero ingresado es {numero}')
else:
    print(f'maximo de intentos')