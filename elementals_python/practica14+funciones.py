#Funciones en python
#basica
#def mi_funcion():
#    print("hola mundo")

#mi_funcion()

#con parametros 

#def suma(x, y):
#    print(x+y)

#suma(10, 10)

#Recursividad


#def factorial(num):
#    if num == 1:
#        return 1
#    else:
#        return (num * factorial(num - 1))

#factor = int(input("Ingrese el numero para calcular el factorial: "))

#print("este es el resultado:", factorial(factor))

#uso de if 

#def numero_positivo(x):
#    if x > 0:
#        print("El numero es positivo")
#    elif x<0:3
#        print("el numero es negativo")
#    elif x == 0:
#        print(" Tu numero cero")

#numero = int(input("ingresa un numero: "))
#numero_positivo(numero)

#Uso de while

def ciclo(x):
    while x <= 10:
        print(x)
        x +=1

numeros = 1
ciclo(numeros)