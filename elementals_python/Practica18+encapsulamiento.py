# Encapsulamiento
class encapsulamiento:
    def __init__(self):
        #self.numero = 0 # esta variable se puede modificar de forma externa
        self.__numero = 0  #si modificamos la variable y agregamos dos __ antes del nombre se vuelve privada
    def operacion(self):
        print(self.__numero + 20)

    def resultado(self):
        return self.__numero
    
ejemplo = encapsulamiento()
ejemplo.operacion()

# de esta forma podemos modificar de forma externa la variable de inicializacion por ejemplo
#default se inicializo en 0 pero de esta forma podemos modificarla
ejemplo.__numero = 100
print(ejemplo.resultado())