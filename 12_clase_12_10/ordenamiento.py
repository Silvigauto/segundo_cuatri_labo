#burbujeo


# lista = [5,7,3,6,5,4,2,1,3,6,9,8]

# c_i = 0
# c_j = 0

# for i in range(len(lista)-1): #verde
#     for j in range (i+1,len(lista)):#naranja
#         if lista[i] > lista[j]:
#             auxiliar = lista[i]
#             lista[i] = lista[j]
#             lista[j] = auxiliar

# for i in range(len(lista)):
#     print(lista[i])


lista = [{"Nombre": "Maria", "Edad": 88},{"Nombre": "Juan", "Edad": 25},{"Nombre": "Eduardo", "Edad": 66},{"Nombre": "Ana", "Edad": 66}]

for i in range(len(lista)-1):#verde
    for j in range(i+1, len(lista)): #naranja
        if lista[i]["Edad"] > lista[j]["Edad"] or \
        (lista[i]["Edad"] == lista[j]["Edad"] and lista[i]["Nombre"]>lista[j]["Nombre"]):
            lista[i],lista[j] = lista[j],lista[i]

for i in range(len(lista)):
    print(f"{lista[i]['Nombre']:20}{lista[i]['Edad']:20}")