numeros = -10

if numeros > 0:
    print("la condicion es positiva")
else:
    print("el numero es negativo")


#practicamos evaluando un numero de entrada
print("Introduce un munero por favor")
numeros = int(input())
if numeros > 0:
    print("el numero es positivo")
if numeros <= 0:
    print("este numero es negativo")
if (numeros % 2) == 0:
    print("Ell numero es par")

# Al usar elif en vez de if se sustituria el metodo switch por lo que cambiar la sentencia elif  al caer en el caso saltaria los demas
