#### pregunta de teoria 8:  de los dos algoritmos, inserción (ordenar_insercion) es estable.
#### Un algoritmo de ordenamiento es estable cuando conserva el orden relativo original de los elementos que tienen el mismo valor en la clave por la que se ordenaa


def _obtener_valor(pokemon, campo):
    if campo == "ataque":
        return pokemon.ataque
    elif campo == "velocidad":
        return pokemon.velocidad
    elif campo == "nro":
        return pokemon.id
    else:
        raise ValueError(f"Campo no válido: {campo}")


def _debe_ir_antes(candidato, actual, descendente):
    if descendente:
        return candidato > actual
    return candidato < actual


def ordenar_seleccion(pokemones, campo, descendente=False):
    n = len(pokemones)

    for i in range(n - 1):
        indice_extremo = i
        valor_extremo = _obtener_valor(pokemones[indice_extremo], campo)

        for j in range(i + 1, n):
            valor_actual = _obtener_valor(pokemones[j], campo)
            if _debe_ir_antes(valor_actual, valor_extremo, descendente):
                indice_extremo = j
                valor_extremo = valor_actual

        if indice_extremo != i:
            pokemones[i], pokemones[indice_extremo] = pokemones[indice_extremo], pokemones[i]

    return pokemones


def ordenar_insercion(pokemones, campo, descendente=False):
    for i in range(1, len(pokemones)):
        actual = pokemones[i]
        valor_actual = _obtener_valor(actual, campo)
        j = i - 1

        while j >= 0:
            valor_comparado = _obtener_valor(pokemones[j], campo)
            if _debe_ir_antes(valor_actual, valor_comparado, descendente):
                pokemones[j + 1] = pokemones[j]
                j -= 1
            else:
                break

        pokemones[j + 1] = actual

    return pokemones