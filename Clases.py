

class Usuario:
    def __init__(self,Id, nombre, apellido, fechanac):
        self.ID = Id
        self.Nombre = nombre
        self.Apellido = apellido
        self.FechaNacimiento = fechanac
    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"