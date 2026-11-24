# pregunta de teoria 2: Quien llama al metodo obtiene un error explicito cuando el Pokemon no existe y evita continuar con un valor invalido.

from ejercicio_01 import Pokemon



class PokemonNoEncontrado(Exception):
    pass


class Pokedex:

    def __init__(self):
        self.pokemones = []

    def agregar(self, pokemon):
        for i in range(len(self.pokemones)):
            if self.pokemones[i].id == pokemon.id:
                self.pokemones[i] = pokemon
                return

        self.pokemones.append(pokemon)

    def obtener(self, id):
        for pokemon in self.pokemones:
            if pokemon.id == id:
                return pokemon

        raise PokemonNoEncontrado("Pokemon no encontrado")

    def listar(self):
        return self.pokemones

    def cantidad(self):
        return len(self.pokemones)


########## prueba para ver si anda

pokedex = Pokedex()

p1 = Pokemon(1, "Bulbasaur", "Planta", "Veneno", 45, 49, 49, 45, 1)
p2 = Pokemon(4, "Charmander", "Fuego", "", 39, 52, 43, 65, 1)

pokedex.agregar(p1)
pokedex.agregar(p2)

print(pokedex.obtener(1))
print(pokedex.cantidad())