from ejercicio_01 import Cancion


def ordenar_por_anio_seleccion(canciones: list) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        idx_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[idx_max].anio:
                idx_max = j
        if idx_max != i:
            canciones[i], canciones[idx_max] = canciones[idx_max], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones: list) -> list:
    """Inserción. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        clave = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > clave.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = clave
    return canciones


if __name__ == "__main__":
    c1 = Cancion(1, "De Musica Ligera", "Soda Stereo", "A", "Rock", 1990, 213)
    c2 = Cancion(12, "Jijiji", "Patricio Rey", "A", "Rock", 1988, 316)
    c3 = Cancion(70, "Ji Ji Ji (Remix)", "Patricio Rey", "A", "Rock", 2020, 300)
    print([c.anio for c in ordenar_por_anio_seleccion([c1, c2, c3])])
    print([c.duracion_seg for c in ordenar_por_duracion_insercion([c1, c2, c3])])

# Teoría:
# Ambos algoritmos (ordenamiento por selección y ordenamiento por inserción) tienen una complejidad temporal de O(n^2) en el peor caso.
# El ordenamiento por inserción es estable, por lo que conserva el orden relativo original entre dos canciones que tengan la misma clave (duración), mientras que selección no lo garantiza debido a los intercambios a distancia.