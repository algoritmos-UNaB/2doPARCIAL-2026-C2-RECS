import os
import struct
from ejercicio_01 import Cancion
from ejercicio_02 import Biblioteca


class ArchivoInvalidoError(Exception):
    pass


FMT_HEADER = "=4s1sI"
SIZE_HEADER = struct.calcsize(FMT_HEADER)  # 9 bytes

FMT_REG = "=I40s40s40s16sHH"
SIZE_REG = struct.calcsize(FMT_REG)  # 144 bytes


def _pack_str(texto: str, ancho: int) -> bytes:
    raw = texto.encode("utf-8")[:ancho]
    return raw.ljust(ancho, b"\x00")


def _unpack_str(raw: bytes) -> str:
    corte = raw.split(b"\x00", 1)[0]
    return corte.decode("utf-8")


def _empaquetar_cancion(c: Cancion) -> bytes:
    return struct.pack(
        FMT_REG,
        c.id,
        _pack_str(c.titulo, 40),
        _pack_str(c.artista, 40),
        _pack_str(c.album, 40),
        _pack_str(c.genero, 16),
        c.anio,
        c.duracion_seg,
    )


def _desempaquetar_cancion(data: bytes) -> Cancion:
    cid, tit, art, alb, gen, anio, dur = struct.unpack(FMT_REG, data)
    return Cancion(
        id=cid,
        titulo=_unpack_str(tit),
        artista=_unpack_str(art),
        album=_unpack_str(alb),
        genero=_unpack_str(gen),
        anio=anio,
        duracion_seg=dur,
    )


def guardar_binario(ruta: str, biblioteca: Biblioteca):
    with open(ruta, "wb") as f:
        header = struct.pack(FMT_HEADER, b"AYED", b"M", biblioteca.cantidad())
        f.write(header)
        for c in biblioteca:
            f.write(_empaquetar_cancion(c))


def cargar_binario(ruta: str) -> Biblioteca:
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    tamanio_archivo = os.path.getsize(ruta)
    if tamanio_archivo < SIZE_HEADER:
        raise ArchivoInvalidoError("El archivo es demasiado chico para contener el encabezado.")

    with open(ruta, "rb") as f:
        header_bytes = f.read(SIZE_HEADER)
        magia, tema, cantidad = struct.unpack(FMT_HEADER, header_bytes)

        if magia != b"AYED" or tema != b"M":
            raise ArchivoInvalidoError("Encabezado inválido: magia o tema incorrectos.")

        tamanio_esperado = SIZE_HEADER + cantidad * SIZE_REG
        if tamanio_archivo != tamanio_esperado:
            raise ArchivoInvalidoError("El tamaño del archivo no coincide con la cantidad de registros.")

        bib = Biblioteca()
        for _ in range(cantidad):
            reg_bytes = f.read(SIZE_REG)
            bib.agregar(_desempaquetar_cancion(reg_bytes))

    return bib


def actualizar_registro(ruta: str, posicion: int, cancion: Cancion):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe.")

    tamanio_archivo = os.path.getsize(ruta)
    if tamanio_archivo < SIZE_HEADER:
        raise ArchivoInvalidoError("Archivo inválido.")

    with open(ruta, "r+b") as f:
        magia, tema, cantidad = struct.unpack(FMT_HEADER, f.read(SIZE_HEADER))
        if magia != b"AYED" or tema != b"M":
            raise ArchivoInvalidoError("Encabezado inválido: magia o tema incorrectos.")
        if tamanio_archivo != SIZE_HEADER + cantidad * SIZE_REG:
            raise ArchivoInvalidoError("El tamaño del archivo está corrupto.")
        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(f"Posición {posicion} fuera de rango (0 a {cantidad - 1}).")

        offset = SIZE_HEADER + posicion * SIZE_REG
        f.seek(offset)
        f.write(_empaquetar_cancion(cancion))


if __name__ == "__main__":
    b = Biblioteca()
    b.agregar(Cancion(1, "De Musica Ligera", "Soda Stereo", "Cancion Animal", "Rock", 1990, 213))
    b.agregar(Cancion(12, "Jijiji", "Patricio Rey", "Baion", "Rock", 1988, 316))
    guardar_binario("test.bin", b)
    actualizar_registro("test.bin", 1, Cancion(12, "Jijiji (Edit)", "Patricio Rey", "Baion", "Rock", 1988, 300))
    b_leida = cargar_binario("test.bin")
    print(b_leida.listar())
    os.remove("test.bin")

# Teoría:
# El registro de posición k (0-based) comienza en el byte:
# offset = tamaño_encabezado + k * tamaño_registro = 9 + k * 144.