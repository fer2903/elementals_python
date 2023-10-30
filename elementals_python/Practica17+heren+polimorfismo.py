#herencia y polimorfismo en python 

class padre:
    # opcional se puede declara variables de inicializacion por ejemplo 
    def __init__(self, numero):
        self.numero = numero  # self. numero es iniciar una nueva variable con valor numero
    def mensaje(self):
        print("hola bunos dias")

    def mensaje2(self):
        print("hola buenas tardes")

    def mensaje3(self):
        print("hola buenas noches")

class hijo(padre):
    # Para accesar al argumento inicializado en la clase padre se utiliza la siguiente sintaxis "polimorfismo" 
    def __init__(self, numero):
        super().__init__(numero) # ahora se puede accedes a la variable declarada en la clase padre
    # Forma menos limpia para inicializar la variable es 
    #def __init__(self, numero):
    #    padre.__init__(self, numero)

    def mensaje4(self):
        print("como has estado")
        print(self.numero + 10)

    def mensaje5(self):
        print("como va la vida")
    
    def mensaje6(self):
        print("hasta luego")

ejemplo = hijo(10)
ejemplo.mensaje()
ejemplo.mensaje5()

ejemplo.mensaje4()