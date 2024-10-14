numero1=int(input("Introduzca un número"))
numero2=int(input("Introduzca otro número"))
operacion=input(" Una operación +,-,*,/")

match operacion:
    case "+":
        resultado=numero1+numero2
        print(f"la suma de {numero1}+{numero2} es {resultado}")
    case "-":
        resultado=numero1-numero2
        print(f"la resta de {numero1}-{numero2} es {resultado}")
    case "*":
        resultado=numero1*numero2
        print(f"la multiplicación de {numero1}*{numero2} es {resultado}")
    case "/":
        resultado=numero1/numero2
        print(f"la división de {numero1}/{numero2} es {resultado}")
    case _:
        print("No valido")