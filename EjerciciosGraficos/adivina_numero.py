import tkinter as tk
import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
intentos = 0
max_intentos = 5

def verificar_numero():
    global intentos
    intentos += 1
    numero_usuario = int(entrada_numero.get())
    
    if numero_usuario < numero_aleatorio:
        resultado.set(f"El número es mayor. Intentos restantes: {max_intentos - intentos}")
    elif numero_usuario > numero_aleatorio:
        resultado.set(f"El número es menor. Intentos restantes: {max_intentos - intentos}")
    else:
        resultado.set("¡Felicidades! Has adivinado el número.")
        return
    
    if intentos >= max_intentos:
        resultado.set(f"Has perdido. El número era: {numero_aleatorio}")
        boton_verificar.config(state=tk.DISABLED)

ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("400x200")

# Entrada de número
tk.Label(ventana, text="Introduce un número entre 1 y 100:").pack(pady=5)
entrada_numero = tk.Entry(ventana, width=10)
entrada_numero.pack(pady=5)

# Botón para verificar el número
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_numero)
boton_verificar.pack(pady=5)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()