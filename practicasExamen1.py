 
#Ejercicio conversor Código Morse


def morse(texto):
    codigo_morse = { 
    'A': '.-', 
    'B': '-...',
    'C': '-.-.', 
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....', 
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.', 
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-',
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-', 
    'Y': '-.--', 
    'Z': '--..', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-', 
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.',
    '0': '-----',
    ' ': '/' }

    texto = texto.upper()
    traduccion = []
    for i in texto:
        if i in codigo_morse:
            traduccion.append(codigo_morse[i])
        else:
            traduccion.append('?')

    return traduccion

  


texto= input("introduce un texto: ")
resultado = morse(texto)
print(resultado)
        


#Ejercicio Las Vueltas en Billetes y Monedas
import random


precio = random.randint(11, 93)

billete = int(input(f"El precio es {precio} €, ¿cuánto me vas a pagar?: "))

resta = (billete - precio)

while(resta > 0):
    if(resta >= 100):
        print("Te devuelvo 100 €")
        resta -= 100
    elif (resta >= 50):
        print("Te devuelvo 50 €")
        resta -=50
    elif(resta >= 20):
        print("Te devuelvo 20 €")
        resta -= 20
    elif(resta >= 10):
        print("Te devuelvo 10 €")
        resta -= 10
    elif(resta >= 5):
        print("Te devuelvo 5 €")
        resta -= 5
    elif(resta >= 2):
        print("Te devuelvo 2 €")
        resta -= 2
    elif (resta >= 1):
        print("Te devuelvo 1 €")
        resta -=1

precio= random.randint(3,97)
billete=int(input(f"el precio es {precio} con cuanto pagara"))
cambio=billete-precio

while(cambio>0):
    match cambio:
        case cambio if (cambio>=100):
            print("tedevuelvo 100")
            cambio-=100
        case cambio if (cambio>=50):
            print("tedevuelvo 50")
            cambio-=50
        case cambio if (cambio>=20):
            print("tedevuelvo 20")
            cambio-=20
        case cambio if (cambio>=10):
            print("tedevuelvo 10")
            cambio-=10
        case cambio if (cambio>=5):
            print("tedevuelvo 5")
            cambio-=5
        case cambio if (cambio>=2):
            print("tedevuelvo 2")
            cambio-=2
        case cambio if (cambio>=1):
            print("tedevuelvo 100")
            cambio-=1

    
            
