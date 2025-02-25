#Crea dos diccionarios: uno con nombres de estudiantes y sus calificaciones en matemáticas, y otro con nombres y calificaciones en ciencias. 
# Combina ambos diccionarios para crear un nuevo diccionario que contenga los estudiantes con sus calificaciones en ambas asignaturas.#

mates = {
    "Mayra":10,
    "Victor":8,
    "Pepe":5,
    "Nuria":8
}
ciencias={
     "Mayra":6,
     "Victor":5,
     "Pepe":4,
     "Nuria":8
}
#nuevo diccionario para almaccebar las clificaciones combinadas
calificaciones_combinadas = {}
#combina las calificacines de mates y ciencias
for i in mates:
    if i in ciencias:
        calificaciones_combinadas[i]={"Matemáticas ": mates[i], 
                                      "ciencias ":ciencias[i]}

#muestra el nuevo diccionario con las calificaciones combinadas       
for i,j in calificaciones_combinadas.items():
    print(i,j)


