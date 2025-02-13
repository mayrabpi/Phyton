from tkinter import*

ventana= Tk()
ventana.config(bg="lightblue")
ventana.title("coloreando")

etiqueta = Label(ventana, text="HOLA MAYRA", bg="blue", fg="white", font=("Comic Sans",16))
etiqueta.pack(pady=20)

boton= Button(ventana, text="Haz click aqui", bg="green", fg="yellow")
boton.pack(pady=10)
ventana.mainloop()