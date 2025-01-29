def mostrar_opcion():
    print(f"Opción seleccionada: {radio_var.get()}")

radio_var = tk.StringVar(value="Opción 1")
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=radio_var, value="Opción 1", command=mostrar_opcion)
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=radio_var, value="Opción 2", command=mostrar_opcion)
radio1.pack()
radio2.pack()