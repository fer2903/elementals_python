# las tuplas son inmutable, se encierran en parentesis
#como usar las tuplas
nombres = ("fernando", "belem", "celeste")
numeros = (1, 2, 2, 2, 5)
valor = (True, False, True, False)
combinada = ("fernando", 1, 2, False)

#print(combinada)
#print(len(numeros))

#acceder a  elementos de una tupla

#print(nombres[1])
#print(combinada[3])
#print(combinada[0:2])
#print(combinada[-1])

#actualizar una tupla
# Para actualizar una tupla se requiere convertir a lista posteriormente modificar la posicion y finalmente revertir y convertir a tupla nuevamente

#x = list(nombres)
#x[1] = "valeria"
#nombres = tuple(x)
#print(nombres)

#desempaquetar una tupla
#para desempaquetar se requiere que el numero de variables sea iggual al numero de valores en la tupla

#(numero1, numero2, numero3, numero4) = numeros
#print(numero1)
#print(numero2)
#print(numero3)
#print(numero4)

#metodos de una tupla: count(), index()

#cuenta el numero de caracteres iguales a 2 
print(numeros.count(2)) 
#obtiene el index del caracter que tengamos en el parentesis

print(numeros.index(5)) 
