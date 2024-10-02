lista=[1,2,3,5,5,6,8,2,7,6,2,8,9,10,11,8,5,6]

print(lista)
numero = int(input("Introduce un numero"))
lista2=[]
valor_mayor=0
for i in lista:
    if i>numero: 
        lista2.append(i)
    if i>valor_mayor:
        valor_mayor=i

lista2.sort()
print(f"Valores mayores que {lista2} , el valor mayo es {valor_mayor}")

