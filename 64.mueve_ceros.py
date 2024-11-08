numeros =[0,1,0,3,12,0,5]
lista=[]
listaCeros=[]

for i in numeros:
    if i==0:
        listaCeros.append(i)
    else:
        lista.append(i)
resultado=listaCeros + lista
print(resultado)

lista.extend(listaCeros)
print(lista)

for index, i in enumerate(lista):
    print(index,i)

lista1 = [5, 9, 10,2,8,6]
print(lista1[::-1])
mi_lista = ["Hola mundo", 3, 4, "pepe"]
mi_lista[1:3] =["hola", "pepe2"]
print(mi_lista)


t =(12345, 54321, 'hello!')
print(t[0]) 
print(t) 
u = t, (1, 2, 3, 4, 5)
print(u) 

tupla=(2,3,4,5)
lontigud_lista = len(tupla)
if lontigud_lista == 1:
 print("Un solo número:", tupla[0])
elif lontigud_lista == 2:
 suma = tupla[0] + tupla[1]
 print("La suma de", tupla[0], "y",tupla[1], "es", suma)
elif lontigud_lista == 3:
 producto = tupla[0] * tupla[1] *tupla[2]
 print("El producto de", tupla[0],tupla[1], "y", tupla[2], "es", producto)
else:
 print("La tupla tiene más de tres")
