from ejercicio_04 import ListaEnlazada

class PilaVaciaError(Exception):
    pass
class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()
    def esta_vacia(self) -> bool:
        return self.lista.esta_vacia()
    def apilar(self, dato):
        self.lista.insertar_al_inicio(dato)
    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede desapilar porque la pila está vacía.")
        return self.lista.quitar_primero()
    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("No se puede ver el tope porque la pila está vacía.")
        return self.lista.primero.dato
class HistorialReproduccion:
    def __init__(self):
        self.pila = Pila()
    def registrar(self, cancion):
        self.pila.apilar(cancion)
    def anterior(self):
        return self.pila.desapilar()
    def ultima(self):
        return self.pila.ver_tope()
'''
TEORÍA

El primer anterior() devuelve "De Música Ligera". Esto pasa porque el historial
usa una pila (estructura LIFO: el último en entrar es el primero en salir), y como
"De Música Ligera" fue la última canción registrada, quedó en el tope y es la primera
que se desapila.
'''