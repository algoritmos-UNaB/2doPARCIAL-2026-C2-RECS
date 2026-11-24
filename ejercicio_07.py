##### preunta teoria 7: No,  porque la busqueda binaria solo funciona correctamente si la lista esta ordenada por el mismo campo sobre el que se busca
 
def busqueda_lineal(pokemones, campo, valor):

    resultado = []

    for pokemon in pokemones:

        if campo == "nombre":
            if pokemon.nombre == valor:
                resultado.append(pokemon)

        elif campo == "tipo":
            if pokemon.tipo1 == valor or pokemon.tipo2 == valor:
                resultado.append(pokemon)

        elif campo == "nro":
            if pokemon.id == valor:
                resultado.append(pokemon)

    return resultado


def busqueda_binaria(pokemones, campo, valor):

    izquierda = 0
    derecha = len(pokemones) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if campo == "nombre":

            dato = pokemones[medio].nombre

            if dato == valor:
                return pokemones[medio]

            if valor < dato:
                derecha = medio - 1
            else:
                izquierda = medio + 1

        elif campo == "nro":

            dato = pokemones[medio].id

            if dato == valor:
                return pokemones[medio]

            if valor < dato:
                derecha = medio - 1
            else:
                izquierda = medio + 1

    return None
