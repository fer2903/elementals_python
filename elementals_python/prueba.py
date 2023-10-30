# importto variables desde el archivo constantes
import constants


numeros  = 12345
print(numeros)
# esto es un comentario 
cadena = "esto es una cadena"
print(cadena) 
#declarar variables multibles
nombre1, nombre2, nombre3 = "1", "2", "3"
print(nombre1) 
print(nombre2) 
print(nombre3) 

#variables con el mismo dato almacenado
apellido1 = apellido2 = apellido3 =  "vargas"

#imprimo constantes
print(constants.PI)

#imprimimos tipo de dato

print(type(constants.PI))
#inserccion de datos externos

print("Me puedes dar tu nombre")

nombre = input()
print(nombre)
print(type(nombre))

# recibir variable con tipo de dato predefinido

print("Me puedes dar un dato")
type_var = int(input())
print(type_var)
print(type(type_var))