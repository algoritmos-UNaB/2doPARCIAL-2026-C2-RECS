# pregunta de la teoria 4:   La referencia al penultimo nodo no esta guardada. En una lista enlazada simple hay que recorrer la lista desde el inicio hasta encontrarlo

from ejercicio_02 import PokemonNoEncontrado


class EquipoLlenoError(Exception):
    pass


class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaEnlazada:

    def __init__(self):
        self.inicio = None
        self._tamanio = 0

    def esta_vacia(self):
        return self.inicio is None

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo
        self._tamanio += 1

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)

        if self.esta_vacia():
            self.inicio = nuevo
        else:
            actual = self.inicio

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        self._tamanio += 1

    def quitar_primero(self):

        if self.esta_vacia():
            return None

        dato = self.inicio.dato
        self.inicio = self.inicio.siguiente
        self._tamanio -= 1

        return dato

    def eliminar(self, id):

        if self.esta_vacia():
            return False

        if self.inicio.dato.id == id:
            self.inicio = self.inicio.siguiente
            self._tamanio -= 1
            return True

        anterior = self.inicio
        actual = self.inicio.siguiente

        while actual is not None:

            if actual.dato.id == id:
                anterior.siguiente = actual.siguiente
                self._tamanio -= 1
                return True

            anterior = actual
            actual = actual.siguiente

        return False

    def buscar(self, id):

        actual = self.inicio

        while actual is not None:

            if actual.dato.id == id:
                return actual.dato

            actual = actual.siguiente

        return None

    def __iter__(self):

        actual = self.inicio

        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Equipo:

    def __init__(self):
        self.pokemones = ListaEnlazada()

    def agregar(self, pokemon):

        if self.cantidad() >= 6:
            raise EquipoLlenoError("Equipo lleno")

        self.pokemones.insertar_al_final(pokemon)

    def quitar(self, id):

        eliminado = self.pokemones.eliminar(id)

        if not eliminado:
            raise PokemonNoEncontrado("Pokemon no encontrado")

    def cantidad(self):
        return self.pokemones.tamanio()

    def __iter__(self):
        return iter(self.pokemones)