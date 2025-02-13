import tkinter as tk

def mayor_menor():
    try:
        num1 = int(entrada_numero1.get())
        num2 = int(entrada_numero2.get())
        if num1 > num2:
            resultado.config(text=f"El número {num1} es mayor que {num2}")
        elif num1 < num2:
            resultado.config(text=f"El número {num2} es mayor que {num1}")
        else:
            resultado.config(text="Los números son iguales")
    except ValueError:
        resultado.config(text="¡Ingresa números válidos!")

        
ventana = tk.Tk()
ventana.title("Introduze el número")


entrada_numero1 = tk.Entry(ventana)
entrada_numero1.grid(row=0, column=0, padx=10, pady=10)

entrada_numero2 = tk.Entry(ventana)
entrada_numero2.grid(row=0, column=1, padx=10, pady=10)


boton_verificar = tk.Button(ventana, text="Verificar", command=mayor_menor)
boton_verificar.grid(row=0, column=2, padx=10, pady=10)


resultado = tk.Label(ventana, text="")
resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()