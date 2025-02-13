import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = operacion_var.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                messagebox.showerror("Error", "No se puede dividir por cero")
                return
            resultado = num1 / num2
        else:
            messagebox.showerror("Error", "Operación no válida")
            return

        # Actualizar el texto del Label con el resultado
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Mini Calculadora")
root.geometry("300x200")

# Campos de entrada
label_num1 = tk.Label(root, text="Número 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Número 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Selección de operación
operacion_var = tk.StringVar(value="+")
label_operacion = tk.Label(root, text="Operación:")
label_operacion.pack()

operaciones = ["+", "-", "*", "/"]
for op in operaciones:
    tk.Radiobutton(root, text=op, variable=operacion_var, value=op).pack()

# Botón para calcular
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.pack()

# Mostrar resultado
label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.pack()

# Iniciar la aplicación
root.mainloop()