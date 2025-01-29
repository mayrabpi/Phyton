import tkinter as tk

# Función que se ejecuta al cambiar el valor de Scale o Spinbox
def mostrar_valor():
    valor_scale = scale.get()
    valor_spinbox = spinbox.get()
    etiqueta.config(text=f"Scale: {valor_scale}, Spinbox: {valor_spinbox}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Scale y Spinbox")

# Crear un Scale (barra deslizante)
scale = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda _: mostrar_valor())
scale.grid(row=0, column=0, padx=10, pady=10)

# Crear un Spinbox (selector numérico)
spinbox = tk.Spinbox(ventana, from_=0, to=100, command=mostrar_valor)
spinbox.grid(row=0, column=1, padx=10, pady=10)

# Crear una etiqueta para mostrar los valores
etiqueta = tk.Label(ventana, text="Scale: 0, Spinbox: 0")
etiqueta.grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()