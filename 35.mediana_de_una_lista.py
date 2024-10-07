#La mediana de una lista es el número central de una lista ordenada. 
# Si la lista tiene número par de elementos, se debe hacer la media 
# aritmética de los elementos centrales para calcular su mediana.

lista=[1,2,3,4,5,6,7,8]

longitud = len(lista)
medianaImpar = lista[longitud//2]
print(medianaImpar)

if longitud%2==0:
    medianaPar=lista[longitud//2]-1+lista[longitud//2]/2
    print(medianaPar)




