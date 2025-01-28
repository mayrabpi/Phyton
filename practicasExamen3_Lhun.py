def algoritmoLuhn(numero):
    """
    Valida un número utilizando el algoritmo de Luhn.

    Args:
        numero (str): El número a validar como una cadena de texto.

    Returns:
        bool: True si el número es válido según el algoritmo de Luhn, False en caso contrario.
    """
    # Convertir el número en una lista de dígitos y revertir su orden usando [::-1]
    digitos = [int(d) for d in numero[::-1]]
    
    suma = 0
    for i, digito in enumerate(digitos):
        if i % 2 == 1:  # Doblar los dígitos en posiciones impares (empezando desde 0)
            digito *= 2
            if digito > 9:  # Si el resultado es mayor que 9, restar 9
                digito -= 9
        suma += digito  # Sumar al total
    
    # El número es válido si la suma es múltiplo de 10
    return suma % 10 == 0

# Ejemplo de uso
numero = "4532015112830366"  # Ejemplo de número válido
if algoritmoLuhn(numero):
    print(f"El número {numero} es válido.")
else:
    print(f"El número {numero} es inválido.")

def lhu(numeros):
    digitos =[int(d) for d in numeros[::-1]]
    suma=0

    for i, digito in enumerate(numeros):
        if i%2==1:
            digito*=2
            if digito>9:
                digito-=9
        suma+=digito

    return digito%10==0