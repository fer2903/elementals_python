#Diccionarios en python

nombres = {1: "fernando", 2: "celeste", 3: "belem", 4: True, 5: False}
tupla = {"nombre": "fernando", "edad": 29, "tup": ("belem", 26, "celeste")}
#print(tupla)

#Acceder  a elementos keys(),  values(), items()

#print(nombres[3])

#print(nombres.keys())
#print(nombres.values())
#print(nombres.items()) # convierte los items en una lista de tuplas separadas

#Cambiar elementos update()

#ejemplo basico
#nombres[3] = "valeria"
#print(nombres)

#nombres.update({3:"belem"})
#print(nombres)

#Agregar elemento


#nombres.update({6:"fer"})
#print(nombres)

# Eliminar elemento pop(), poItem(), del, clear()

#nombres.pop(5)
#print(nombres)

# elimina el ultimo valor
#nombres.popitem() 
#print(nombres)

#Limpia el diccionario
#nombres.clear()
#print(nombres)

#Borrar valor 

del nombres[1]
print(nombres)