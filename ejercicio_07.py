from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError


def busqueda_lineal(canciones: list, campo: str, valor: str) -> list:
    if campo not in ("titulo", "artista", "genero"):
        raise ValueError(f"Campo de búsqueda inválido: {campo}")

    encontradas = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            encontradas.append(cancion)
    return encontradas


def busqueda_binaria_por_titulo(canciones_ordenadas: list, titulo: str) -> Cancion:
    izq = 0
    der = len(canciones_ordenadas) - 1

    while izq <= der:
        medio = (izq + der) // 2
        actual = canciones_ordenadas[medio]
        if actual.titulo == titulo:
            return actual
        elif actual.titulo < titulo:
            izq = medio + 1
        else:
            der = medio - 1

    raise CancionNoEncontradaError(f"No se encontró la canción con título '{titulo}'.")


if __name__ == "__main__":
    c1 = Cancion(15, "Alfonsina y el mar", "Mercedes Sosa", "A", "Folklore", 1969, 298)
    c2 = Cancion(1, "De Musica Ligera", "Soda Stereo", "A", "Rock", 1990, 213)
    c3 = Cancion(12, "Jijiji", "Patricio Rey", "A", "Rock", 1988, 316)
    print(busqueda_lineal([c1, c2, c3], "genero", "Rock"))
    print(busqueda_binaria_por_titulo([c1, c2, c3], "Jijiji"))

# Teoría:
# La búsqueda binaria exige que la lista esté ordenada por título porque en cada paso compara el elemento central con el buscado para descartar la mitad izquierda o la mitad derecha del arreglo; sin orden, ese descarte no sería válido.
# Sobre n canciones, la búsqueda binaria tiene complejidad O(log n) en el peor caso, mientras que la búsqueda lineal por artista tiene complejidad O(n).