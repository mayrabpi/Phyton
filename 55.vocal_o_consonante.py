letra = input("Introduce una letra: ")
match letra.lower():
    case "a"|"e"|"i"|"o"|"u":
        print(f"{letra} Es vocal")
    case "b"|"c"|"d"|"f"|"g"|"h"|"j"|"l"|"m"|"n"|"ñ"|"p"|"q"|"r"|"s"|"t"|"v"|"w"|"x"|"y"|"z":
        print(f"{letra} Es consonante")
    case _:
        print(f"{letra} Es un carácter no válido")

#otra forma usando isalpha()
letra1 = input("Introduce una letra: ")
match letra1.lower():
    case "a"|"e"|"i"|"o"|"u":
        print("Es vocal")
    case letra1 if letra1.isalpha():
        print("Es consonante")
    case _:
        print("Es un Carácter no válido")
 
    
    
    
    