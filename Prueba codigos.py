class Mascota:
# Constructor y atributos
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

# Método (acción)
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy un {self.especie}"


# Creando un objeto de tipo "Mascota"
mi_perro = Mascota("Rex", "Perro")
print(mi_perro.saludar())


