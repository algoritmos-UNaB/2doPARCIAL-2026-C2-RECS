import csv
import os
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


ENCABEZADO_ESPERADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


def guardar_canciones_csv(ruta: str, biblioteca: Biblioteca):
    with open(ruta, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(ENCABEZADO_ESPERADO)
        for c in biblioteca:
            writer.writerow([c.id, c.titulo, c.artista, c.album, c.genero, c.anio, c.duracion_seg])


def cargar_canciones_csv(ruta: str) -> Biblioteca:
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    bib = Biblioteca()
    try:
        with open(ruta, mode="r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=",")
            encabezado = next(reader, None)
            if encabezado != ENCABEZADO_ESPERADO:
                raise ArchivoInvalidoError("El encabezado del CSV no coincide con el formato esperado.")

            for num_fila, fila in enumerate(reader, start=2):
                if len(fila) < 7:
                    raise ArchivoInvalidoError(f"La fila {num_fila} tiene menos columnas de las esperadas.")
                cancion = Cancion(
                    id=int(fila[0]),
                    titulo=fila[1],
                    artista=fila[2],
                    album=fila[3],
                    genero=fila[4],
                    anio=int(fila[5]),
                    duracion_seg=int(fila[6]),
                )
                bib.agregar(cancion)
    except ArchivoInvalidoError:
        raise
    except Exception as e:
        raise ArchivoInvalidoError(f"Error al procesar el archivo CSV: {e}")

    return bib


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    guardar_canciones_csv("test_canciones.csv", b)
    b2 = cargar_canciones_csv("test_canciones.csv")
    print(b2.listar())
    os.remove("test_canciones.csv")

# Teoría:
# Sí, hay que recorrer secuencialmente las filas anteriores porque el CSV es un archivo de texto con registros de longitud variable (cada título o artista tiene distinta cantidad de caracteres), por lo que no se puede calcular de antemano el byte exacto donde empieza la fila 50.