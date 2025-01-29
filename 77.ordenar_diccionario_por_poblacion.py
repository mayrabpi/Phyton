#Crea un diccionario de países y su población. Ordena el diccionario en función de la población de los países, de mayor a menor, y muestra el resultado.

diccionario={
    "España":300,
    "Francia":200,
    "Peru":400
}


for (nombre,poblacion) in diccionario.items():

    print(f"{nombre}:{sorted(poblacion)}")

    



    