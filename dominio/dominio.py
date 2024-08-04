
class CuerpoCeleste:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

class Planeta(CuerpoCeleste):
    def __init__(self, id, nombre, tipo, radio, distanciaSol):
        super().__init__(id, nombre, tipo)
        self.radio = radio
        self.distanciaSol = distanciaSol

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        self._radio = radio

    @property
    def distanciaSol(self):
        return self._distanciaSol

    @distanciaSol.setter
    def distanciaSol(self, distanciaSol):
        self._distanciaSol = distanciaSol