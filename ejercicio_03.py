from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca, CancionNoEncontradaError


def versiones_de(biblioteca: Biblioteca, versiones: list, cancion_id: int) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    # Verificamos que la canción exista (si no existe, obtener lanza CancionNoEncontradaError)
    biblioteca.obtener(cancion_id)

    # Buscamos las versiones directas de cancion_id
    directas = []
    for cid, vid, tipo in versiones:
        if vid == cancion_id:
            directas.append((cid, tipo))

    # Ordenamos de menor a mayor cancion_id (burbujeo simple para no usar .sort)
    n = len(directas)
    for i in range(n):
        for j in range(0, n - i - 1):
            if directas[j][0] > directas[j + 1][0]:
                directas[j], directas[j + 1] = directas[j + 1], directas[j]

    # Caso base implicito: si directas está vacía, el bucle no corre y devuelve []
    resultado = []
    for cid, tipo in directas:
        cancion_derivada = biblioteca.obtener(cid)
        resultado.append((cancion_derivada.titulo, tipo))
        # Llamada recursiva en preorden
        sub_versiones = versiones_de(biblioteca, versiones, cid)
        resultado.extend(sub_versiones)

    return resultado


if __name__ == "__main__":
    bib = Biblioteca()
    bib.agregar(Cancion(12, "Jijiji", "Patricio Rey", "Album", "Rock", 1988, 316))
    bib.agregar(Cancion(13, "Ji Ji Ji", "Patricio Rey", "En Directo", "Rock", 1992, 318))
    bib.agregar(Cancion(70, "Ji Ji Ji (Remix)", "Patricio Rey", "Remixes", "Rock", 2020, 300))
    vers = [(13, 12, "live"), (70, 13, "remix")]
    print(versiones_de(bib, vers, 12))

# Teoría:
# Caso base: Cuando ninguna tupla en la lista de versiones tiene como version_de_id al cancion_id consultado (es decir, no tiene versiones directas), la función retorna una lista vacía [].
# Secuencia de llamadas para versiones_de(..., 12):
# 1. versiones_de(..., 12) encuentra la versión directa 13 ("Ji Ji Ji", "live") y llama a versiones_de(..., 13).
# 2. versiones_de(..., 13) encuentra la versión directa 70 ("Ji Ji Ji (Remix)", "remix") y llama a versiones_de(..., 70).
# 3. versiones_de(..., 70) cae en el caso base (nadie deriva de 70) y devuelve [].
# 4. versiones_de(..., 13) recibe [] de 70, arma su lista y devuelve [("Ji Ji Ji (Remix)", "remix")].
# 5. versiones_de(..., 12) recibe eso de 13, lo concatena detrás de la 13 y devuelve [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")].