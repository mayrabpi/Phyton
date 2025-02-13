def mostrar_ticket_compra():
      carrito=[]
      if carrito:
           resultado_texto = "\n--- Ticket de Compra ---\n"
           total = 0
           for item in carrito:
            subtotal = item["cantidad"] * item["precio"]
            total += subtotal
            resultado_texto += f"{item['nombre']} - Cantidad: {item['cantidad']} - Precio Unitario: {item['precio']}€ - Subtotal: {subtotal}€\n"
            resultado_texto += f"Total a pagar: {total}€"
           else:
            resultado_texto = "No se realizaron compras."
    
    except ValueError:
        resultado.delete(1.0, tk.END)
        resultado.insert(tk.END, "Error: Por favor, ingrese valores válidos para cantidad y precio.") resultado.delete(1.0, tk.END)
    resultado.insert(tk.END, resultado_texto)
    popup.destroy()
