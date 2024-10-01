cadena= input("Introduce una cadena")
palabras = cadena.split()
contador=0
for i in range(len(palabras)) :
    contador+=1
print(contador)

#otra forma
contarPalabras=len(palabras)
print(contarPalabras) 