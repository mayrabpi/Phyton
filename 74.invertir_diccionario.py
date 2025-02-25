# Función para invertir un diccionario
"""
def invertir_diccionario(diccionario):
    # Crear un nuevo diccionario vacío para almacenar el resultado invertido
    diccionario_invertido = {}

    # Recorrer cada par clave-valor en el diccionario original
    for clave, valor in diccionario.items():
        # Añadir el valor original como nueva clave y la clave original como nuevo valor
        diccionario_invertido[valor] = clave

    # Devolver el diccionario invertido
    return diccionario_invertido
ciudades_codigos_postales = {
    "Madrid": 28001,
    "Barcelona": 28340,
    "Valencia": 46001,
    "Sevilla": 41001,
    "Zaragoza": 50001
}

codigos_postales_ciudades = invertir_diccionario(ciudades_codigos_postales)


print(codigos_postales_ciudades)"""



ciudades_codigos_postales = {
    "Madrid": 28001,
    "Barcelona": 28340,
    "Valencia": 46001,
    "Sevilla": 41001,
    "Zaragoza": 50001
}
invertido ={}
for i,j in ciudades_codigos_postales.items():
    invertido[j]=i
print(invertido)