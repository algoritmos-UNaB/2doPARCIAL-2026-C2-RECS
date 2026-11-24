class CancionNoEncontradaError(Exception):
    pass
class Biblioteca:
    def __init__(self):
        self.canciones = []
    def agregar(self, cancion):
        self.canciones.append(cancion)
    def cantidad(self):
        return len(self.canciones)
    def obtener(self, id):
        for cancion in self.canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No se encontró ninguna canción con el id {id}.")
    def listar(self):
        return [str(cancion) for cancion in self.canciones]
    def __iter__(self):
        return iter(self.canciones)
'''
TEORÍA

La biblioteca guarda el catálogo completo de todas las canciones disponibles.
En cambio, una playlist guarda solamente una selección de esas canciones en un orden específico para reproducirlas.
'''