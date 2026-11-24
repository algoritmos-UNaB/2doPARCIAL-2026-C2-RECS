#### pregunta de teoria 9: Si, hace falta leer los anteriores; el acceso en un archivo de texto CSV es secuencial

import csv


class ArchivoInvalidoError(Exception):
    pass


def guardar_csv(ruta, pokedex):

    encabezado = [
        "id",
        "nombre",
        "tipo1",
        "tipo2",
        "hp",
        "ataque",
        "defensa",
        "velocidad",
        "generacion",
    ]

    with open(ruta, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(encabezado)

        for pokemon in pokedex:
            escritor.writerow([
                pokemon.id,
                pokemon.nombre,
                pokemon.tipo1,
                pokemon.tipo2 if pokemon.tipo2 is not None else "",
                pokemon.hp,
                pokemon.ataque,
                pokemon.defensa,
                pokemon.velocidad,
                pokemon.generacion,
            ])


def cargar_csv(ruta):

    encabezado_esperado = [
        "id",
        "nombre",
        "tipo1",
        "tipo2",
        "hp",
        "ataque",
        "defensa",
        "velocidad",
        "generacion",
    ]

    try:
        with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo, delimiter=",")
            filas = list(lector)
    except OSError as exc:
        raise ArchivoInvalidoError(f"No se pudo abrir o leer el archivo: {ruta}") from exc

    if not filas or filas[0] != encabezado_esperado:
        raise ArchivoInvalidoError("El archivo no tiene el encabezado esperado.")

    pokemones = []

    for fila in filas[1:]:

        if len(fila) != 9:
            raise ArchivoInvalidoError("La fila no tiene exactamente 9 columnas.")

        try:
            id_pokemon = int(fila[0])
            nombre = fila[1]
            tipo1 = fila[2]
            tipo2 = fila[3] if fila[3] != "" else None
            hp = int(fila[4])
            ataque = int(fila[5])
            defensa = int(fila[6])
            velocidad = int(fila[7])
            generacion = int(fila[8])
        except ValueError as exc:
            raise ArchivoInvalidoError("Uno de los campos numéricos no es válido.") from exc

        pokemones.append(
            Pokemon(
                id=id_pokemon,
                nombre=nombre,
                tipo1=tipo1,
                tipo2=tipo2,
                hp=hp,
                ataque=ataque,
                defensa=defensa,
                velocidad=velocidad,
                generacion=generacion,
            )
        )

    return Pokedex(pokemones)