def dar_cambio(costo, pagado):
    # Verificar si el pago es suficiente
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

# Ejemplo de uso
dar_cambio(21, 50)
