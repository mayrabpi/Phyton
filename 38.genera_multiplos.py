numero=int(input("Introduce un número: "))
cantidad= int(input("Introduce un número: "))
multiplos=[]
for i in range(1,cantidad+1):
    multiplos.append(numero*i)

print(f"Estos son los {cantidad} primeros multiplos de {numero} : {multiplos}")
   

