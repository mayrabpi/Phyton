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
print(mi_lista.index(2))#devuelve la posición del elemento 2

lista=["hola mundo",3,4,"pepe"]
lista[1:3]=["hola","pepe2"]#cambia los elementos de la lista
print(lista)
lista2=[1,2,3]
lista3=[0,1,2,3]
print(3 in lista2 )
print (lista2==lista3)
for i in lista2:
    print(i)

y=[1,2,3,4,5]
for index, i in enumerate(y):
    print(index,i)

frutas=["pera","uva"]
for indice, i in enumerate(frutas):
    print(indice,i)

m=[5,9,10]
n=["jazz","Rock","jent"]
for i1,i2 in zip(n,m):
       print(i1,i2)

lista_1=[10,"Phyton",False,[4,5,6]]
print(lista_1[0]+5)
print(lista_1[1].upper())
print(lista_1[2]or True)

if "Phyton" in lista_1:
     print("la palabra phyton esta en la lista")

lista_1[3][0]=100
print(mi_lista[3][1])










