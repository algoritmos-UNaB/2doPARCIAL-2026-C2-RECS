from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self._cant = 0

    def esta_vacia(self) -> bool:
        return self.primero is None

    def tamanio(self) -> int:
        return self._cant

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato, self.primero)
        self.primero = nuevo
        self._cant += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self._cant += 1

    def quitar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía.")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        self._cant -= 1
        return dato

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._lista = ListaEnlazada()

    def agregar(self, cancion: Cancion):
        self._lista.insertar_al_final(cancion)

    def quitar(self, id: int):
        anterior = None
        actual = self._lista.primero
        while actual is not None:
            if actual.dato.id == id:
                if anterior is None:
                    self._lista.primero = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                self._lista._cant -= 1
                return
            anterior = actual
            actual = actual.siguiente
        raise CancionNoEncontradaError(f"La canción con id {id} no está en la playlist.")

    def listar(self) -> list:
        return [str(c) for c in self._lista]

    def duracion_total(self) -> int:
        total = 0
        for c in self._lista:
            total += c.duracion_seg
        return total


if __name__ == "__main__":
    pl = Playlist()
    pl.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    pl.agregar(Cancion(12, "Jijiji", "Patricio Rey", "Baion", "Rock", 1988, 316))
    print(pl.listar(), "Total:", pl.duracion_total())

# Teoría:
# Cuando ya hay n elementos y solo se guarda referencia al primer nodo, se recorren exactamente n nodos (desde el primero hasta el último cuya referencia siguiente es None) para poder enlazar el nuevo nodo al final.