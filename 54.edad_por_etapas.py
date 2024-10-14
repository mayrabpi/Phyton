edad= int(input("Introduce su edad: "))
#niño= range(0,12)
match edad:
    case edad if(edad>=0 and edad<=12):
        print("Eres un niño")
    case edad if(edad>=13 and edad<=17):
        print("Eres Adolescente")
    case edad if(edad>=18 and edad<=64):
        print("Eres Adulto")
    case edad if(edad>=65 ):
        print("Eres Anciano")
    case _:
        print(" Edad no valida")

#otra forma 
match edad:
    case edad if(0<=edad<=12):
        print("Eres un niño")
    case edad if(13<=edad<=17):
        print("Eres Adolescente")
    case edad if(18<=edad<=64):
        print("Eres Adulto")
    case edad if(edad>=65 ):
        print("Eres Anciano")
    case _:
        print(" Edad no valida")
