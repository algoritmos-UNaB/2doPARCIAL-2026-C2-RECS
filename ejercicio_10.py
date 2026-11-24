import struct
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca
from ejercicio_09 import ArchivoInvalidoError

FMT_ENCABEZADO = "=4s1sI"
TAM_ENCABEZADO = struct.calcsize(FMT_ENCABEZADO)  # 9 bytes
FMT_REGISTRO = "=I40s40s40s16sHH"
TAM_REGISTRO = struct.calcsize(FMT_REGISTRO)  # 144 bytes
MAGIA = b"AYED"
TEMA = b"M"
def _empaquetar_texto(texto, ancho):
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")
def _desempaquetar_texto(datos):
    return datos.split(b"\x00", 1)[0].decode("utf-8")
def _empaquetar_cancion(cancion):
    return struct.pack(
        FMT_REGISTRO,
        cancion.id,
        _empaquetar_texto(cancion.titulo, 40),
        _empaquetar_texto(cancion.artista, 40),
        _empaquetar_texto(cancion.album, 40),
        _empaquetar_texto(cancion.genero, 16),
        cancion.anio,
        cancion.duracion_seg,
    )
def _validar_encabezado(archivo):
    archivo.seek(0, 2)
    tam_archivo = archivo.tell()
    archivo.seek(0)
    if tam_archivo < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es más chico que el encabezado.")
    magia, tema, cantidad = struct.unpack(FMT_ENCABEZADO, archivo.read(TAM_ENCABEZADO))
    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia del archivo no es AYED.")
    if tema != TEMA:
        raise ArchivoInvalidoError("El tema del archivo no es M.")
    if tam_archivo != TAM_ENCABEZADO + cantidad * TAM_REGISTRO:
        raise ArchivoInvalidoError("El tamaño del archivo no coincide con la cantidad de registros.")
    return cantidad
def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FMT_ENCABEZADO, MAGIA, TEMA, biblioteca.cantidad()))
        for cancion in biblioteca:
            archivo.write(_empaquetar_cancion(cancion))
def cargar_binario(ruta) -> Biblioteca:
    try:
        with open(ruta, "rb") as archivo:
            cantidad = _validar_encabezado(archivo)
            biblioteca = Biblioteca()
            for _ in range(cantidad):
                datos = archivo.read(TAM_REGISTRO)
                id_c, tit, art, alb, gen, anio, dur = struct.unpack(FMT_REGISTRO, datos)
                cancion = Cancion(
                    id_c,
                    _desempaquetar_texto(tit),
                    _desempaquetar_texto(art),
                    _desempaquetar_texto(alb),
                    _desempaquetar_texto(gen),
                    anio,
                    dur,
                )
                biblioteca.agregar(cancion)
            return biblioteca
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"No se encontró el archivo '{ruta}'.")
def actualizar_registro(ruta, posicion, cancion):
    try:
        with open(ruta, "r+b") as archivo:
            cantidad = _validar_encabezado(archivo)
            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError(f"La posición {posicion} está fuera de rango.")
            offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO
            archivo.seek(offset)
            archivo.write(_empaquetar_cancion(cancion))
    except FileNotFoundError:
        raise ArchivoInvalidoError(f"No se encontró el archivo '{ruta}'.")
'''
TEORÍA

El registro de posición k empieza en el byte 9 + k * 144
(tamaño del encabezado + k * tamaño del registro), ya que la posición arranca en 0.
'''