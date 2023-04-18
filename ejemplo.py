# Definición de la clase Padre
class Padre:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        print("Hola, soy el padre.")

# Definición de la clase Hijo que hereda de Padre
class Hijo(Padre):
    def __init__(self, nombre, edad, hobbies):
        super().__init__(nombre, edad)
        self.hobbies = hobbies

    def hablar(self):
        print("Hola, soy el hijo.")

    def mostrar_hobbies(self):
        print("Mis hobbies son:", ", ".join(self.hobbies))

# Creación de objetos de la clase Hijo
hijo1 = Hijo("Juan", 25, ["correr", "leer", "bailar"])
hijo2 = Hijo("Pedro", 20, ["jugar videojuegos", "tocar guitarra"])

# Accediendo a atributos y métodos de los objetos
print(hijo1.nombre)
hijo2.hablar()
hijo1.mostrar_hobbies()