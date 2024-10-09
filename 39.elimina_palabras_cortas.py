#Elimina palabras cortas
lista_palabra=["hola","como","te","llamas"]
print(lista_palabra)
for i in lista_palabra:
    if len(i)< 4:
        lista_palabra.remove(i)
print(lista_palabra)



