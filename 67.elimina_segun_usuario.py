lista=[1,1,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,5]
print(f"Lista original: {lista}")
n=int(input("Introduce un número : "))
lista1=[]

for i in lista:
    if (lista.count(i)<=n):
        lista1.append(i)

print(f"Lista filtrada: {lista1}")

