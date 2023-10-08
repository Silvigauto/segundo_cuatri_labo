import json
#una funcion que reciba la lista que se vaya a asignar a la clave del diccionario
#funcion parser
'''
data = {}
data['clientes'] = []
data['clientes'].append({"nombre":"luis", "edad":24})
data['clientes'].append({"nombre":"maria", "edad":33})
data['clientes'].append({"nombre":"juan", "edad":22})

#si no existe lo crea, si existe lo pisa
with open("clientes.json", 'w') as archivo:
    json.dump(data, archivo, indent=4)
'''

#el json devuelve un diccionario
with open("clientes.json", "r") as archivo:
    data = json.load(archivo)

lista = data["clientes"]
print(lista[0])