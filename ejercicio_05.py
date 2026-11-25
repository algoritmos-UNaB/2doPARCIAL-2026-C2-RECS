from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:
    def __init__(self):
        self._lista = ListaEnlazada()

    def apilar(self, dato):
        self._lista.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar: la pila está vacía.")
        return self._lista.quitar_primero()

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No hay tope: la pila está vacía.")
        return self._lista.primero.dato

    def esta_vacia(self) -> bool:
        return self._lista.esta_vacia()


class HistorialReproduccion:
    def __init__(self):
        self._pila = Pila()

    def registrar(self, cancion: Cancion):
        self._pila.apilar(cancion)

    def anterior(self) -> Cancion:
        return self._pila.desapilar()

    def ultima(self) -> Cancion:
        return self._pila.ver_tope()


if __name__ == "__main__":
    h = HistorialReproduccion()
    h.registrar(Cancion(12, "Jijiji", "PR", "A", "Rock", 1988, 316))
    h.registrar(Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "A", "Folklore", 1969, 298))
    h.registrar(Cancion(1, "De Musica Ligera", "Soda Stereo", "A", "Rock", 1990, 213))
    print("Anterior:", h.anterior())

# Teoría:
# El primer anterior() devuelve "De Música Ligera".
# Esto ocurre porque la pila sigue una política LIFO (Last In, First Out: último en entrar, primero en salir), por lo que la última canción registrada queda en el tope y es la primera en desapilarse.