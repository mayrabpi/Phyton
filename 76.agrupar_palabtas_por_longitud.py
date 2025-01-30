#Dada una lista de palabras, agrúpalas en un diccionario donde las claves 
# sean los números que representan la longitud de las palabras, y los valores sean listas de palabras de esa longitud.
# Lista de palabras de ejemplo
palabras = ["mayra", "python",  "geniales", "programacion", "divertido"]

# Diccionario para almacenar las palabras agrupadas por longitud
agrupadas_por_longitud = {}


for palabra in palabras:
    longitud = len(palabra)
    if longitud not in agrupadas_por_longitud:
        agrupadas_por_longitud[longitud] = []
    agrupadas_por_longitud[longitud].append(palabra)

print(agrupadas_por_longitud)

