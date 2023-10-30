#Cadenas en python
#Las cadenas se encierran en corchetes y sonmutables
#cadena simple
nombre = "Fernando {}"
edad = 29
#Cadena con saltos de linea 

nombres = """fernando
belem
celeste"""

#print(nombres)
#Trabajar con una cadena

#for x in nombre:
#    print(x)

#print(len(nombre))


#Cortar cadenas.

#print(nombre[-8])
#print(nombre[2])
#print(nombre[0:3])

#Cadenas y sus metodos: upper(), lower(), replace(), format()

print(nombre.upper())
print(nombre.lower())
print(nombre.replace("F", "p"))
print(nombre.format(29))