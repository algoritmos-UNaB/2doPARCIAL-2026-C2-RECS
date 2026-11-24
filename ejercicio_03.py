# pregunra de la teoria  3: descendientes(4) -----> descendientes(5) -----> descendientes(6)

from ejercicio_02 import PokemonNoEncontrado


def descendientes(origen_id, pokedex, aristas):

    pokedex.obtener(origen_id)

    resultado = []

    for origen, destino in aristas:

        if origen == origen_id:

            pokedex.obtener(destino)

            resultado.append(destino)

            resultado.extend(descendientes(destino, pokedex, aristas))

    return resultado