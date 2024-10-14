figura=int(input("Introduce cuantos lados:"))
match figura:
    case 1:
        print("Es una Recta")
    case 2:
        print("Es un Digono")
    case 3:
        print("Es un Triángulo")
    case 4:
        print("Es un cuadrilatero")
    case 5:
        print("Es un Hexágono")
    case 6:
        print("Es un Heptagono")
    case _:
        print("")