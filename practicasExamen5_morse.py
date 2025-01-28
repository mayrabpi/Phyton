def textoACodigoMorse(texto):
    """
    Traduce una cadena de texto a código Morse.

    Args:
        texto (str): Cadena de texto a traducir.

    Returns:
        str: Traducción de la cadena en código Morse.
    """
    # Diccionario que contiene el mapeo de caracteres a código Morse
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', 
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', "'": '.----.', '!': '-.-.--',
        '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
        ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
        
        '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
    }
    texto= texto.upper()
    morse=[]
    for i in texto:
        if i in morse_dict:
            morse.append(morse_dict[i])
        else:
            morse.append('?')

    return morse





texto= input("introduce un texto: ")
traduccion= textoACodigoMorse(texto)
print("traduccuon")
print(traduccion)


  

"""

# Convertir el texto a mayúsculas para simplificar el mapeo
    texto = texto.upper()

    # Traducir cada carácter al código Morse correspondiente
    codigo_morse = []
    for i in texto:
        if i in morse_dict:
            codigo_morse.append(morse_dict[i])
        else:
            codigo_morse.append('?')  # Usar '?' para caracteres no reconocidos

    # Unir los códigos Morse con espacios entre ellos
    return ' '.join(codigo_morse)

# Ejemplo de uso
texto = input("Ingrese un texto para traducir a código Morse: ")
traduccion = textoACodigoMorse(texto)
print("Traducción en código Morse:")
print(traduccion)

"""
    
    

