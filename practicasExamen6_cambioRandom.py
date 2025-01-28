import random

def dar_cambio():
    # Generar un precio aleatorio entre $1 y $100
    costo = random.randint(11, 93)
    print(f"El costo del artículo es: ${costo}")
    
    # Solicitar al usuario el importe pagado

    pagado = int(input("¿Con cuánto vas a pagar? (ingresa un número entero): "))

    # Verificar si el importe pagado es suficiente
    if pagado < costo:
        print("El importe pagado es insuficiente.")
        return
    
    # Calcular el cambio total
    cambio = pagado - costo
    print(f"Cambio total: ${cambio}")
    
    # Denominaciones disponibles
    billetes = [20, 10, 5, 2, 1]
    resultado = {}
    
    # Calcular el número mínimo de billetes
    for billete in billetes:
        if cambio >= billete:
            cantidad = cambio // billete
            cambio %= billete
            resultado[billete] = cantidad
    
    # Imprimir el resultado
    print("Cambio en billetes:")
    for billete, cantidad in resultado.items():
        print(f"${billete}: {cantidad}")

# Ejecutar la función
dar_cambio()


