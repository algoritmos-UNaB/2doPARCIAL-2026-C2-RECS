# pregunta de teroia 5: Quedaria B en el tope y esta disciplina se llama LIFO 

from ejercicio_04 import ListaEnlazada


class PilaVaciaError(Exception):
    pass


class Pila:

    def __init__(self):
        self.datos = ListaEnlazada()

    def apilar(self, dato):
        self.datos.insertar_al_inicio(dato)

    def desapilar(self):

        if self.esta_vacia():
            raise PilaVaciaError("Pila vacia")

        return self.datos.quitar_primero()

    def ver_tope(self):

        if self.esta_vacia():
            raise PilaVaciaError("Pila vacia")

        return self.datos.inicio.dato

    def esta_vacia(self):
        return self.datos.esta_vacia()


class HistorialAcciones:

    def __init__(self):
        self.acciones = Pila()

    def registrar(self, accion):
        self.acciones.apilar(accion)

    def deshacer(self):
        return self.acciones.desapilar()

    def ultima(self):
        return self.acciones.ver_tope()
