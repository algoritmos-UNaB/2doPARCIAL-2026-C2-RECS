######## pregunta de teoria 6: Porque una cola trabaja con la disciplina FIFO (First In, First Out), por lo que sale primero el elemento que entro primero

from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:

    def __init__(self):
        self.datos = ListaEnlazada()

    def encolar(self, dato):
        self.datos.insertar_al_final(dato)

    def desencolar(self):

        if self.esta_vacia():
            raise ColaVaciaError("Cola vacia")

        return self.datos.quitar_primero()

    def ver_frente(self):

        if self.esta_vacia():
            raise ColaVaciaError("Cola vacia")

        return self.datos.inicio.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class ColaTurnos:

    def __init__(self):
        self.cola = Cola()

    def encolar(self, pokemon):
        self.cola.encolar(pokemon)

    def siguiente(self):
        return self.cola.desencolar()

    def proximo(self):
        return self.cola.ver_frente()