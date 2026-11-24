from ejercicio_01 import Cancion
from ejercicio_02 import CancionNoEncontradaError

def busqueda_lineal(canciones, campo, valor) -> list:
    resultado = []
    for cancion in canciones:
        if campo == "titulo" and cancion.titulo == valor:
            resultado.append(cancion)
        elif campo == "artista" and cancion.artista == valor:
            resultado.append(cancion)
        elif campo == "genero" and cancion.genero == valor:
            resultado.append(cancion)
    return resultado
def busqueda_binaria_por_titulo(canciones_ordenadas, titulo) -> Cancion:
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
'''
TEORÍA

La búsqueda binaria necesita la lista ordenada por título porque en cada paso compara el título buscado con el del 
medio para decidir si seguir en la mitad izquierda o en la derecha; si estuviera desordenada, al descartar 
una mitad podría perder la canción. Sobre n canciones, la búsqueda binaria tiene complejidad O(log n) porque reduce el
rango de búsqueda a la mitad en cada paso. La búsqueda lineal por artista tiene complejidad O(n) porque
tiene que recorrer las n canciones para encontrar todas las coincidencias.
'''