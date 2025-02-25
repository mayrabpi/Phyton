import tkinter as tk

def verificar_contraseña():
    contraseña = entrada_contraseña.get()
    if len(contraseña) < 8:
        resultado.set("La contraseña debe tener al menos 8 caracteres.")
        return

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    caracteres_especiales = 0
    caracteres_especiales_lista = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

    for char in contraseña:
        if char.isupper():
            tiene_mayuscula = True
        elif char.islower():
            tiene_minuscula = True
        elif char.isdigit():
            tiene_numero = True
        elif char in caracteres_especiales_lista:
            caracteres_especiales += 1

    if not tiene_mayuscula:
        resultado.set("La contraseña debe tener al menos una letra mayúscula.")
    elif not tiene_minuscula:
        resultado.set("La contraseña debe tener al menos una letra minúscula.")
    elif not tiene_numero:
        resultado.set("La contraseña debe tener al menos un número.")
    elif caracteres_especiales < 2:
        resultado.set("La contraseña debe tener al menos dos caracteres especiales.")
    else:
        resultado.set("La contraseña es válida.")

ventana = tk.Tk()
ventana.title("Verificador de Contraseña")
ventana.geometry("400x200")

# Entrada de contraseña
tk.Label(ventana, text="Contraseña:").pack(pady=5)
entrada_contraseña = tk.Entry(ventana, width=50)
entrada_contraseña.pack(pady=5)

# Botón para verificar la contraseña
tk.Button(ventana, text="Verificar", command=verificar_contraseña).pack(pady=5)

# Resultado
resultado = tk.StringVar()
tk.Label(ventana, textvariable=resultado).pack(pady=20)

ventana.mainloop()