import re



# nombres = ['josé', 'carlos', 'ana']
# apellidos = ['gomez', 'ruiz', 'perez']
# edades = [20,19,34]
# delimitador = ','
# with open("agenda.csv", 'w', encoding='utf-8') as arhivo:
#     for i in range(len(nombres)):
#         mensaje = f'{nombres[i]},{apellidos[i]},{edades[i]}\n'  # con ; se guarda en cada celda separada en excel
#         #mensaje =delimitador.join([nombres[i], apellidos[i], str(edades[i]),"\n"])
#         arhivo.write(mensaje)

#funciones parsear, son leer el archivo y convertilo en otra cosa
def parsear_agenda(path:str)->list:
    agenda = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as archivo:
        for linea in archivo:
            registro = re.split(",|\n", linea)
            contacto = {}
            contacto['nombre'] = registro[0]
            contacto['apellido'] = registro[1]
            contacto['edad'] = registro[2]
            agenda.append(contacto)
    
    return agenda

mi_agenda = parsear_agenda('agenda.csv')
if len(mi_agenda) != 0: 
    for contacto in mi_agenda:
        print(f"{contacto['nombre']:20}{contacto['apellido']:20}{contacto['edad']}")



'''
#el objeto file es iterable
with open('agenda.csv', 'r') as archivo:
    for linea in archivo:
        # registro = linea.split(',')
        registro = re.split(",|\n", linea)
        print(f"{registro[0]}-{registro[1]}-{registro[2]}")
'''