mi_lista=[1,2,"hola",True,3]
mi_lista.append(4)#agrega el elemento 4 al final

print(mi_lista)
mi_lista.remove("hola")#quita el elemento "hola"
print(mi_lista)
print(mi_lista)
print(len(mi_lista))#imprime la longitud de la lista
mi_lista.pop()#quita el último elemento
print(mi_lista)
mi_lista.insert(1,"pepe")#inserta el elemento "pepe" en la posición 1
print(mi_lista)
mi_lista.extend([5,6,7])#agrega los elementos 5,6,7 al final
print(mi_lista)
mi_lista.index(5)#devuelve la posición del elemento 5
mi_lista.count(5)#devuelve el numero de veces que aparece el elemento 5
#mi_lista.sort()#ordena la lista
print(mi_lista)
mi_lista_1=[2,1,3,4,8,6,7,5,9,10]
print(mi_lista.count(2))#devuelve el numero de veces que aparece el elemento mi_lista_1
print(mi_lista_1)
mi_lista_1.sort()#ordena la lista
print(mi_lista_1)
mi_lista_1.clear()#borra la lista
print(mi_lista_1)
mi_lista_2=mi_lista.copy()#copia la lista
print(mi_lista_2)






