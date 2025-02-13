#Dado un diccionario con nombres de empleados y sus edades, crea un nuevo diccionario que contenga solo los empleados 
# mayores de 30 años. Usa bucles for y condicionales para filtrar los valores.
diccionario = {"Mayra": 25, "Pepito": 32, "Pedri": 28, "Elena": 35, "María": 30, "Luisa": 40}
empleados_mayores = {}
for empleado, edad in diccionario.items():
    if edad > 30:
        empleados_mayores[empleado] = edad
        
print(empleados_mayores)