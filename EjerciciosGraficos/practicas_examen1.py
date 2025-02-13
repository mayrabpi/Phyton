from tkinter import*

ventana = Tk()
ventana.geometry("300x300")
ventana.title("practicando para el examen")
cuadroNombre = Entry(ventana)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)

cuadroApellido= Entry(ventana)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroEmail= Entry(ventana)
cuadroEmail.grid(row=2,column=1,padx=10,pady=10)

nombreLabel= Label(ventana, text="Nombre")
nombreLabel.grid(row=0,column=0,padx=10,pady=10)

apellidoLabel= Label(ventana, text="Apellido")
apellidoLabel.grid(row=1,column=0,padx=10,pady=10)

emailLabel= Label(ventana, text="Direccion Email")
emailLabel.grid(row=2,column=0,padx=10,pady=10)

resultado = Text(ventana,height=5,width=15)
resultado.grid(row=4, column=1)

boton1= Button(text="Enviar")
boton1.grid(column=1)







ventana.mainloop()