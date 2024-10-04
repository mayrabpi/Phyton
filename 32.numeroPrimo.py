primos = []
num = int(input("Dame un numero: "))
for i in range(2, num + 1):
    contador = 0  
    for j in range(1, i + 1):
        if i % j == 0:
            contador += 1
    if contador == 2:  
        primos.append(i)

print("Números primos:",primos)








     




    
