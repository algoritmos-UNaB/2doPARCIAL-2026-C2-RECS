from ejercicio_01 import Cancion 
class CancionNoEncontradaError(Exception): 
    pass

class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion: Cancion):
        #evitamos duplicados por id
        for c in self._canciones:
            if c == cancion:
                return
            self._canciones.append(cancion)

    def cantidad(self) -> int:
        return len(self._canciones)

    def obtener(self, id: int) -> Cancion:
        for c in self._canciones:
            if c.id == id:
                return c
            raise CancionNoEncontradaError(f"No se encontro ninguna cancion con id {id} en la biblioteca")

    def listar(self) -> list:
        res = []
        for c in self._canciones:
            res.append(str(c))
        return res

    def __iter__(self):
        return iter(self._canciones)


if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    print(bib.listar())

# Teoria:
# La biblioteca funciona como el catalogo general unico que almacena todas las canciones disponibles en el sistema.
# Por otro lado, una playlist guarda una seleccion personalizada y ordenada de canciones elegidas por el usuario, 
# permitiendo incluso repetir temas o armar secuencias particulares sin alterar el catalogo base.