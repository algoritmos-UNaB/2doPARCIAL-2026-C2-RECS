# pregunta de teoria  2: Quien llama al metodo obtiene un error explicito cuando el Pokemon no existe y evita continuar con un valor invalido

from ejercicio_01 import Pokemon



class PokemonNoEncontrado(Exception):
    pass


class Pokedex:
    def __init__(self):
        self._pokemones = []

    def agregar(self, pokemon):
        for i in range(len(self._pokemones)):
            if self._pokemones[i].id == pokemon.id:
                self._pokemones[i] = pokemon
                return
        self._pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self._pokemones:
            if pokemon.id == id:
                return pokemon