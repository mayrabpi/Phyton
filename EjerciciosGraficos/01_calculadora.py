import tkinter as tk

# Función para calcular la suma
def calcular_suma():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.config(text=f"Resultado: {num1 + num2}")
    except ValueError:
        resultado.config(text="¡Ingresa números válidos!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Simple")

# Crear cuadros de entrada
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=0, padx=10, pady=10)

entrada2 = tk.Entry(ventana)
entrada2.grid(row=0, column=1, padx=10, pady=10)

# Crear botón para calcular
boton_sumar = tk.Button(ventana, text="Sumar", command=calcular_suma)
boton_sumar.grid(row=1, column=0, columnspan=2, pady=10)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado: ")
resultado.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()