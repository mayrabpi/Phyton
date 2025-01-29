#Crea dos diccionarios: uno con nombres de estudiantes y sus calificaciones en matemáticas, y otro con nombres y calificaciones en ciencias. 
# Combina ambos diccionarios para crear un nuevo diccionario que contenga los estudiantes con sus calificaciones en ambas asignaturas.#

mates = {
    "Mayra":10,
    "Victor":8,
    "Pepe":5,
    "Nuria":8
}
calificacionesCiencias={
     "Mayra":6,
     "Victor":5,
     "Pepe":4,
     "Nuria":8
}

nuevoDiccionario={}

for i,j in mates.items():
    print(i,j)

