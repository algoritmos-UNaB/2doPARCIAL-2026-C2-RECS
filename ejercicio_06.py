from ejercicio_01 import Cancion
from ejercicio_04 import ListaEnlazada


class ColaVaciaError(Exception):
    pass


class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar: la cola está vacía.")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No hay frente: la cola está vacía.")
        return self._lista.primero.dato

    def esta_vacia(self) -> bool:
        return self._lista.esta_vacia()


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion: Cancion):
        self._cola.encolar(cancion)

    def siguiente(self) -> Cancion:
        return self._cola.desencolar()

    def que_sigue(self) -> Cancion:
        return self._cola.ver_frente()


if __name__ == "__main__":
    cr = ColaReproduccion()
    cr.encolar_cancion(Cancion(12, "Jijiji", "PR", "A", "Rock", 1988, 316))
    cr.encolar_cancion(Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "A", "Folklore", 1969, 298))
    cr.encolar_cancion(Cancion(1, "De Musica Ligera", "Soda Stereo", "A", "Rock", 1990, 213))
    print("Siguiente:", cr.siguiente())

# Teoría:
# El primer siguiente() devuelve "Jijiji".
# A diferencia de la pila del ejercicio 5 (LIFO), la cola respeta el orden de llegada FIFO (First In, First Out: primero en entrar, primero en salir), reproduciendo las canciones en el mismo orden en que fueron encoladas.