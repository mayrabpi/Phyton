#Dada una lista de palabras, filtra aquellas que comienzan con una
#letra dada por el usuario.
palabras=["sol","luna","mar","estrella","cielo"]
letra=input("introduce una inicial").lower()
filtrado=[]

for i in palabras:
   if i.startswith(letra):
      filtrado.append(i)

print (f"Las palabras que empiezan por {letra} son {filtrado}")
      
    

