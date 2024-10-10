letra=input("introduce una inicial").lower()
palabras=["sol","luna","mar","estrella","cielo","suma","soniquete"]

filtradas=[]

for i in palabras:
    if i[0].lower()==letra:
        filtradas.append(i)
print(f"Plabras que comienzan con {letra}: {filtradas}")