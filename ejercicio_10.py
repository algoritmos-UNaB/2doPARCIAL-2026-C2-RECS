# TEORIA: El tamano fijo del encabezado (9 bytes) y el tamano fijo de cada registro (56 bytes) permiten calcular el desplazamiento en bytes: offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO.

import struct

from ejercicio_09 import ArchivoInvalidoError


FORMATO_ENCABEZADO = "<4scI"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO)  # 9 bytes

FORMATO_REGISTRO = "<I20s12s12s4H"
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)  # 56 bytes

MAGIA_ESPERADA = b"AYED"
TEMA_ESPERADO = b"P"


def _codificar_texto(texto, ancho):
    if texto is None:
        texto = ""
    raw = texto.encode("utf-8")[:ancho]
    return raw.ljust(ancho, b"\x00")


def _decodificar_texto(raw):
    return raw.split(b"\x00", 1)[0].decode("utf-8")


def _empaquetar_pokemon(pokemon):
    return struct.pack(
        FORMATO_REGISTRO,
        pokemon.id,
        _codificar_texto(pokemon.nombre, 20),
        _codificar_texto(pokemon.tipo1, 12),
        _codificar_texto(pokemon.tipo2, 12),
        pokemon.hp,
        pokemon.ataque,
        pokemon.defensa,
        pokemon.velocidad,
    )


def _leer_encabezado(archivo):
    encabezado_bytes = archivo.read(TAM_ENCABEZADO)
    if len(encabezado_bytes) < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es más corto que el encabezado.")

    magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, encabezado_bytes)
    if magia != MAGIA_ESPERADA or tema != TEMA_ESPERADO:
        raise ArchivoInvalidoError("Encabezado binario inválido (magia o tema incorrectos).")

    return cantidad


def guardar_binario(ruta, pokedex):
    pokemones = list(pokedex)
    cantidad = len(pokemones)

    with open(ruta, mode="wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA_ESPERADA, TEMA_ESPERADO, cantidad))
        for pokemon in pokemones:
            archivo.write(_empaquetar_pokemon(pokemon))


def cargar_binario(ruta):
    try:
        with open(ruta, mode="rb") as archivo:
            cantidad = _leer_encabezado(archivo)
            pokemones = []

            for _ in range(cantidad):
                registro_bytes = archivo.read(TAM_REGISTRO)
                if len(registro_bytes) < TAM_REGISTRO:
                    raise ArchivoInvalidoError("Archivo binario truncado o incompleto.")

                (
                    pokemon_id,
                    nombre_raw,
                    tipo1_raw,
                    tipo2_raw,
                    hp,
                    ataque,
                    defensa,
                    velocidad,
                ) = struct.unpack(FORMATO_REGISTRO, registro_bytes)

                nombre = _decodificar_texto(nombre_raw)
                tipo1 = _decodificar_texto(tipo1_raw)
                tipo2_texto = _decodificar_texto(tipo2_raw)
                tipo2 = tipo2_texto if tipo2_texto != "" else None

                pokemones.append(
                    Pokemon(
                        id=pokemon_id,
                        nombre=nombre,
                        tipo1=tipo1,
                        tipo2=tipo2,
                        hp=hp,
                        ataque=ataque,
                        defensa=defensa,
                        velocidad=velocidad,
                        generacion=1,
                    )
                )
    except OSError as exc:
        raise ArchivoInvalidoError(f"No se pudo leer el archivo binario: {ruta}") from exc

    return Pokedex(pokemones)


def actualizar_registro(ruta, posicion, pokemon):
    try:
        with open(ruta, mode="r+b") as archivo:
            cantidad = _leer_encabezado(archivo)

            if posicion < 0 or posicion >= cantidad:
                raise ArchivoInvalidoError("La posición del registro está fuera de rango.")

            offset = TAM_ENCABEZADO + posicion * TAM_REGISTRO
            archivo.seek(offset)
            archivo.write(_empaquetar_pokemon(pokemon))
    except OSError as exc:
        raise ArchivoInvalidoError(f"No se pudo actualizar el archivo binario: {ruta}") from exc