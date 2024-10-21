lista = [1, "hola", 3.14, True, 42, "mundo", False, ["a","b"]]

enteros = []
cadenas = []
booleanos = []
decimales=[]
otros = []

for elemento in lista:
    match elemento:
        case True|False:
            booleanos.append(elemento)
        case int():
            enteros.append(elemento)
        case str():
            cadenas.append(elemento)
        case float():
            decimales.append(elemento)

        case _:
            otros.append(elemento)

print("Números enteros:", enteros)
print("Cadenas de texto:", cadenas)
print("Booleanos:", booleanos)
print("Todos los decimales:", decimales)
print("Otros tipos de datos:", otros)