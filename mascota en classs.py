 
class Mascota:

    def asignar_nombre(self, nombre_mascota):
        self.nombre = nombre_mascota 
        print(f"Nombre asignado: {self.nombre}")

    def asignar_especie(self, especie_mascota):
        self.especie = especie_mascota 
        print(f"Especie asignada: {self.especie}")

    def presentarse(self):
        
        if hasattr(self, 'nombre') and hasattr(self, 'especie'):
            print(f"Me llamo {self.nombre} y soy un(a) {self.especie}.")
        else:
            print("Aún no tengo toda la información.")

# Crear un objeto Mascota
mascota1 = Mascota()

# Intentar presentarse antes de asignar información
print("\nIntento 1 de presentación:")
mascota1.presentarse() # Salida: Aún no tengo toda la información.

# Asignar nombre
print("\nAsignando información:")
mascota1.asignar_nombre("ochi")


print("\nIntento 2 de presentación:")
mascota1.presentarse() 
# Asignar especie
mascota1.asignar_especie("Perro")

# Presentarse con toda la información
print("\nIntento 3 de presentación:")
mascota1.presentarse() 
# Crear otra mascota y asignar atributos directamente (menos común sin _init_)
mascota2 = Mascota()
mascota2.nombre = "luli"
mascota2.especie = "Gato"
print("\nPresentación mascota 2:")
mascota2.presentarse() #

