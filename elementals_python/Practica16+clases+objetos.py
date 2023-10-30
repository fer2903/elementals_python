# Clases y objetos
#clase de forma sencilla ejemplo 1
#class miPrimeraClase:
    #atributod de clase
    ######
    #siempre se debe iniciar de esta forma para inicializar los valores
    # Atributos de instancia
#    def __init__(self):
#        print("hola munod mi primera clase en python")
    # metodos
#    def mensaje(self):
#        print("buenas tardes")
#    def mensaje2(self):
#        print("adios")

#mensaje = miPrimeraClase()
#mensaje.mensaje()
#mensaje.mensaje2()
#print(type(mensaje.__init__))
#print(type(mensaje.mensaje))
#print(type(mensaje.mensaje2))


class clase2:
    def __init__(self, numero):
        #atributos de instancia
        self.numero = numero
    def comparar(self):
        if self.numero > 0:
            print("El numero es positivo")
        elif self.numero < 0:
            print("El numero es menor a cero")
        elif self.numero == 0:
            print("el numero es negativo")
        
    def ciclo_clase2(self):
        while self.numero <=10:
            print(self.numero)
            self.numero +=1

#ejemplo = clase2(0)
#ejemplo.comparar()
#ejemplo.ciclo_clase2()

ejemplo = clase2(int(input("Introduce un numero: ")))
ejemplo.comparar()
ejemplo.ciclo_clase2()