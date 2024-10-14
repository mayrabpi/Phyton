numero=int(input("Introduce un número del 1 al 3 digitos: "))

match len(str(numero)):
    case 3:
        print(f"Centenas: {str(numero)[0]}, Decenas: {str(numero)[1]},Unidades: {str(numero)[2]}")
    case 2:
         print(f"Decenas: {str(numero)[0]},Unidades: {str(numero)[1]}")
    case 1:
         print(f"unidades: {str(numero)[0]}")


