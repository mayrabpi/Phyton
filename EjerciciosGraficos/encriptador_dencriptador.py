import tkinter as tk

def encriptar(mensaje):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    encriptado = ''
    for letra in mensaje:
        if letra.lower() in alfabeto:
            indice = alfabeto.index(letra.lower())
            nuevo_indice = (indice + 3) % 26  # Desplazamiento fijo de 3
            nueva_letra = alfabeto[nuevo_indice]
            if letra.isupper():
                nueva_letra = nueva_letra.upper()
            encriptado += nueva_letra
        else:
            encriptado += letra
    return encriptado

def desencriptar(mensaje):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    desencriptado = ''
    for letra in mensaje:
        if letra.lower() in alfabeto:
            indice = alfabeto.index(letra.lower())
            nuevo_indice = (indice - 3) % 26  # Desplazamiento fijo de 3
            if nuevo_indice < 0:
                nuevo_indice += 26
            nueva_letra = alfabeto[nuevo_indice]
            if letra.isupper():
                nueva_letra = nueva_letra.upper()
            desencriptado += nueva_letra
        else:
            desencriptado += letra
    return desencriptado

def encriptar_mensaje():
    mensaje = entrada_mensaje.get()
    mensaje_encriptado = encriptar(mensaje)
    resultado.set(f"Mensaje encriptado: {mensaje_encriptado}")

def desencriptar_mensaje():
    mensaje = entrada_mensaje.get()
    mensaje_desencriptado = desencriptar(mensaje)
    resultado.set(f"Mensaje desencriptado: {mensaje_desencriptado}")

ventana = tk.Tk()
ventana.title("Encriptador/Desencriptador")
ventana.geometry("400x300")

# Entrada de mensaje
tk.Label(ventana, text="Mensaje:").pack(pady=5)
entrada_mensaje = tk.Entry(ventana, width=50)
entrada_mensaje.pack(pady=5)

# Botones de encriptar y desencriptar
tk.Button(ventana, text="Encriptar", command=encriptar_mensaje).pack(pady=5)
tk.Button(ventana, text="Desencriptar", command=desencriptar_mensaje).pack(pady=5)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()