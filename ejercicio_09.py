import csv
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca

class ArchivoInvalidoError(Exception):
    pass
ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]
def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(ENCABEZADO)
        for cancion in biblioteca:
            escritor.writerow([
                cancion.id,
                cancion.titulo,
                cancion.artista,
                cancion.album,
                cancion.genero,
                cancion.anio,
                cancion.duracion_seg,
            ])
def cargar_canciones_csv(ruta) -> Biblioteca:
    try:
        with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            encabezado = next(lector, None)
            if encabezado != ENCABEZADO:
                raise ArchivoInvalidoError("El encabezado del CSV no coincide con el esperado.")
            biblioteca = Biblioteca()
            for num_fila, fila in enumerate(lector, start=2):
                if len(fila) < len(ENCABEZADO):
                    raise ArchivoInvalidoError(f"La fila {num_fila} tiene menos columnas de las esperadas.")
                try:
                    cancion = Cancion(
                        int(fila[0]),
                        fila[1],
                        fila[2],
                        fila[3],
                        fila[4],
                        int(fila[5]),
                        int(fila[6]),
                    )
                except ValueError:
                    raise ArchivoInvalidoError(f"La fila {num_fila} tiene datos numéricos inválidos.")
                biblioteca.agregar(cancion)
            return biblioteca
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"No se encontró el archivo '{ruta}'.")
'''
TEORÍA

Sí, hay que recorrer las filas anteriores porque en un CSV cada línea tiene longitud
variable según los textos que guarda, así que no se puede calcular en qué byte empieza
la fila 50 sin leer secuencialmente los saltos de línea previos.
'''