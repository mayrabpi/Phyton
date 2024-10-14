diaSemana=input("Introduce un dia de la semana:")
match diaSemana.lower():
    case "lunes":
        print(" Es laborable")
    case "martes":
        print("Es laborable")
    case "miercoles":
        print ("Es laborable")
    case "viernes":
        print("Es laborable")
    case "sabado":
        print(" No Laborable")
    case "domingo":
        print(" No Laborable")
    case _:
        print("No es un día valido")
    
    
