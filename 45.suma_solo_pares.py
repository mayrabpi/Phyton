lista=[1,2,3,4,5,6,7,8]
suma=0

for i in lista:
    if i%2==0:
       suma+=i


print(f"la suma de los pares de {lista} es {suma}")