def createMagicPotion(potions, goal):
    """
    Encuentra los índices de las dos primeras pociones que sumen exactamente el poder objetivo.
    
    Args:
        potions (list): Lista de enteros que representan los poderes de las pociones.
        goal (int): Poder objetivo.

    Returns:
        tuple: Una tupla con los índices de las dos pociones, o "No encontrado" si no existe.
    """
    indices = {}  # Diccionario para almacenar el índice de cada poder ya visto
    
    for i, poder in enumerate(potions):
        complemento = goal - poder  # Necesitamos encontrar este número en la lista
        
        if complemento in indices:
            # Si el complemento ya está en el diccionario, devolvemos los índices
            return (indices[complemento], i)
        
        # Almacenar el índice actual en el diccionario
        indices[poder] = i
    
    return "No encontrado"  # Si no encontramos ninguna combinación

# Ejemplo de uso
potions = [4, 5, 6, 2]
goal = 8
resultado = createMagicPotion(potions, goal)
print(resultado)


def crearPociones(pociones, objetivo):
    for i in range(len(pociones)):
        for j in range(i+1, len(pociones)):
            if pociones[i]+ pociones[j]==objetivo:
                return(i,j)
    return "none"

   


pociones = [4,5,6,2]
objetivo=11
resultado= crearPociones(pociones, objetivo)
print(resultado)


"""
otra forma menos eficiente pero mas facil de entender funciona igual
  for i in range(len(potions)):  # Primer bucle para la primera poción
        for j in range(i + 1, len(potions)):  # Segundo bucle para la segunda poción
            if potions[i] + potions[j] == goal:  # Verificar si suman el objetivo
                return (i, j)  # Devolver los índices si se cumple la condición
    return "No encontrado"  # Si no se encuentra ninguna combinación
"""
