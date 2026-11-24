# pregunta de teoria 8:  De los dos algoritmos, insercion es estable; un algoritmo de ordenamiento es estable cuando conserva el orden relativo original de los elementos que tienen el mismo valor en el campo por el que se ordena


def ordenar_seleccion(pokemones, campo, descendente):

    n = len(pokemones)

    for i in range(n - 1):

        indice_extremo = i

        if campo == "ataque":
            valor_extremo = pokemones[indice_extremo].ataque
        elif campo == "velocidad":
            valor_extremo = pokemones[indice_extremo].velocidad
        elif campo == "nro":
            valor_extremo = pokemones[indice_extremo].id

        for j in range(i + 1, n):

            if campo == "ataque":
                valor_actual = pokemones[j].ataque
            elif campo == "velocidad":
                valor_actual = pokemones[j].velocidad
            elif campo == "nro":
                valor_actual = pokemones[j].id

            if descendente:
                es_mejor = valor_actual > valor_extremo
            else:
                es_mejor = valor_actual < valor_extremo

            if es_mejor:
                indice_extremo = j
                valor_extremo = valor_actual

        if indice_extremo != i:
            pokemones[i], pokemones[indice_extremo] = pokemones[indice_extremo], pokemones[i]

    return pokemones


def ordenar_insercion(pokemones, campo, descendente):

    for i in range(1, len(pokemones)):

        actual = pokemones[i]

        if campo == "ataque":
            valor_actual = actual.ataque
        elif campo == "velocidad":
            valor_actual = actual.velocidad
        elif campo == "nro":
            valor_actual = actual.id

        j = i - 1

        while j >= 0:

            if campo == "ataque":
                valor_comparado = pokemones[j].ataque
            elif campo == "velocidad":
                valor_comparado = pokemones[j].velocidad
            elif campo == "nro":
                valor_comparado = pokemones[j].id

            if descendente:
                debe_moverse = valor_actual > valor_comparado
            else:
                debe_moverse = valor_actual < valor_comparado

            if debe_moverse:
                pokemones[j + 1] = pokemones[j]
                j -= 1
            else:
                break

        pokemones[j + 1] = actual

    return pokemones