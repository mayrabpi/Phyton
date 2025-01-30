import tkinter as tk

# Función para convertir Celsius a Fahrenheit
def convertir_temperatura():
    try:
        celsius = float(entrada_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        resultado.config(text="¡Ingresa un número válido!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Convertidor de Temperatura")

# Crear cuadro de entrada para Celsius
entrada_celsius = tk.Entry(ventana)
entrada_celsius.grid(row=0, column=0, padx=10, pady=10)

# Crear botón para convertir
boton_convertir = tk.Button(ventana, text="Convertir", command=convertir_temperatura)
boton_convertir.grid(row=1, column=0, pady=10)

# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.grid(row=2, column=0, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()