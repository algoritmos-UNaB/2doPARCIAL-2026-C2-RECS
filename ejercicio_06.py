from ejercicio_04 import ListaEnlazada

class ColaVaciaError(Exception):
    pass
class Cola:
    def __init__(self):
        self.lista = ListaEnlazada()
    def esta_vacia(self) -> bool:
        return self.lista.esta_vacia()
    def encolar(self, dato):
        self.lista.insertar_al_final(dato)
    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede desencolar porque la cola está vacía.")
        return self.lista.quitar_primero()
    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("No se puede ver el frente porque la cola está vacía.")
        return self.lista.primero.dato
class ColaReproduccion:
    def __init__(self):
        self.cola = Cola()
    def encolar_cancion(self, cancion):
        self.cola.encolar(cancion)
    def siguiente(self):
        return self.cola.desencolar()
    def que_sigue(self):
        return self.cola.ver_frente()
'''
TEORÍA

El primer siguiente() devuelve "Jijiji". La cola funciona con orden FIFO, así que las canciones 
salen en el mismo orden en que se encolaron. Se diferencia de la pila del ejercicio 5 porque 
la pila usa orden LIFO, por eso ahí devolvía "De Música Ligera" que había sido la última en registrarse.
'''