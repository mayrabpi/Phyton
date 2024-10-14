temperatura=int(input("Introduce la temperatura: "))
match temperatura:
    case temperatura if(temperatura<0):
        print("Muy frio")
    case temperatura if(0<=temperatura<=10):
        print("Frio")
    case temperatura if(11<=temperatura<=20):
        print("Templado")
    case temperatura if(21<=temperatura<=30):
        print("Calor")
    case temperatura if(temperatura>30):
        print("Muy caliente")
    case _:
        print("No contemplado")

