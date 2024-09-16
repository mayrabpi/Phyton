numeroDado = int(input("Dime un número para calcular su factorial"))
factorial=1
for i in range(1,numeroDado+1):
    factorial*=i

print("el factorial de ", numeroDado, " es ", factorial)

