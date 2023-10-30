
def suma(x, y):
    print(x + y)

def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num -1))

def es_positivo(num):
    if num > 0:
        print("el numero es positivo")
    elif num < 0:
        print("El numero es negativo")
    elif num == 0:
        print("El numero es 0")

def ciclo(num):
    while num <= 10:
        print(num)
        num +=1