#Crea un diccionario de países y su población. Ordena el diccionario en función de la población de los países, de mayor a menor, y muestra el resultado.

diccionario={
    "España":300,
    "Francia":200,
    "Peru":400
}


lista_paises= list(diccionario.items())

# Ordenar la lista de tuplas manualmente por población de mayor a menor
for i in range(len(lista_paises)):
    for j in range(i + 1, len(lista_paises)):
        if lista_paises[i][1] < lista_paises[j][1]:
            lista_paises[i], lista_paises[j] = lista_paises[j], lista_paises[i]

diccionario_ordenado = dict(lista_paises)
for pais, poblacion in diccionario_ordenado.items():
    print(f"{pais}: {poblacion}")


    



    