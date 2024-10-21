tupla=(3,4)
longitud_tupla =len(tupla)

if longitud_tupla ==1:
    print(f"un solo numero: {tupla[0]}")
elif longitud_tupla ==2:
    suma =tupla[0]+tupla[1]
    print(f"la suma de {tupla[0]} y {tupla[1]} es {suma}")
elif longitud_tupla==3:
    producto = tupla[0]*tupla[1]*tupla[3]
    print(f"la multi{producto}")
else:
    print("la tupla tiene mas de 3 números")



#diccionario
diccionario_1={"Nombre":"Sierra","edad":25}
print(diccionario_1)

diccionario_2=([("Nombre","sierra"),("edad",25)])
print(diccionario_2)

diccionario_1["Nombre"]="Victor"
print(diccionario_1)
diccionario_1["curso"]="2º Dam"
print(diccionario_1)

for i in diccionario_1:
    print(i)

for i in diccionario_1:
    print(i,":",diccionario_1[i])

for i,j in diccionario_1.items():#imprimir clave valor
    print(i,":",j)

d={"a":1,"b":2,"c":3,"d":4}
print(d.get("a"))
print(d.get("d"))
print(d.get("d","no existe"))

it =d.items()
print(it)
print(it)

print(list(d))
print(list(d)[0][0])

k=d.keys()
print(k)
print(list(k))


v=d.values()
print(v)
print(list(v))

d.pop("a")
print(d)

d.popitem()
print(d)

d1={"a":1,"b":2}
d2={"a":0,"d":400}
d1.update(d2)
print(d1)