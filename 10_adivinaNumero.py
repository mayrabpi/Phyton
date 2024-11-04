import random

numero_secreto = random.randint(1,10)
intentos =0
print("Adivina el número secreto entre 1 y 100!")

while True:
    intento = int(input("Ingresa tu número:"))
    intentos +=1

    if intento == numero_secreto:
        print("Adivinaste el numero en ", intentos, " intentos.")
        break
    elif intento<numero_secreto:
        print("mayor, mayor")
    else:
        print("menor, menor")


numero= random.randint(1,10)
intentos=0

while True:
    intento= int(input("ingresa un numero"))
    intentos+=1

    if intento==numero:
        print("adivinaste el numero")
        break
    elif intento<numero:
        print("mayor")
    else:
        print("menor")