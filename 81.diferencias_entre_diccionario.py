#Dado un diccionario con nombres de alumnos y sus calificaciones en un examen, y otro con sus calificaciones en un segundo examen, 
#crea un nuevo diccionario que contenga los alumnos cuyas calificaciones mejoraron en el segundo 
# examen

calificaciones_examen1={"Mayra":6,"Victor":8,"Pepe":5,"Nuria":7}
calificaciones_examen2={"Mayra":8,"Victor":8,"Pepe":6,"Nuria":5}

calificaciones_mejoradas={}
for alumno, calificacion1 in calificaciones_examen1.items():
    if alumno in calificaciones_examen2:
        calificacion2= calificaciones_examen2[alumno]
        if calificacion2>calificacion1:
            calificaciones_mejoradas[alumno]=calificacion2

print(calificaciones_mejoradas)

 