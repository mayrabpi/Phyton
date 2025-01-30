# Diccionario de ejemplo con nombres de estudiantes y sus calificaciones
calificaciones = {
    "Juan": [85, 90, 78],
    "María": [92, 88, 84],
    "Pedro": [70, 75, 80],
    "Ana": [100, 95, 98]
}

# Nuevo diccionario para almacenar los promedios
promedios = {}

# Calcular el promedio de calificaciones de cada estudiante
for estudiante, notas in calificaciones.items():
    promedio = sum(notas) / len(notas)
    promedios[estudiante] = promedio

# Imprimir el diccionario con los promedios
print(promedios)