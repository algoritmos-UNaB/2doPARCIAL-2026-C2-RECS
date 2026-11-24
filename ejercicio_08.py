def ordenar_por_anio_seleccion(canciones) -> list:
    """Selección. Año de mayor a menor."""
    n = len(canciones)
    for i in range(n - 1):
        idx_max = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[idx_max].anio:
                idx_max = j
        canciones[i], canciones[idx_max] = canciones[idx_max], canciones[i]
    return canciones


def ordenar_por_duracion_insercion(canciones) -> list:
    """Inserción. duracion_seg de menor a mayor."""
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones


'''
TEORÍA

Ambos algoritmos (selección e inserción) tienen complejidad O(n^2) en el peor caso.

El que conserva el orden relativo de dos canciones con la misma clave es inserción
(es un algoritmo estable), porque solo corre hacia la derecha los elementos que son
estrictamente mayores al actual. En cambio, selección hace intercambios entre
posiciones que pueden estar lejos y eso puede romper el orden original entre
elementos con la misma clave.
'''