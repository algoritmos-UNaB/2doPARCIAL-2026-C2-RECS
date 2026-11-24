# pregunta de teoria: La identidad es el id y el estado son los demás atributos, no, la identidad no debería cambiar después de construido el objeto

class Pokemon:
    def __init__(
        self,
        id,
        nombre,
        tipo1,
        tipo2,
        hp,
        ataque,
        defensa,
        velocidad,
        generacion
    ):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        if self.tipo2 != "":
            return f"#{self.id} {self.nombre} ({self.tipo1}/{self.tipo2})"
        return f"#{self.id} {self.nombre} ({self.tipo1})"

    def __eq__(self, otro):
        return isinstance(otro, Pokemon) and self.id == otro.id

### para comprobar si funcionaba correctamente mas que nada
p1 = Pokemon(1, "Bulbasaur", "Planta", "Veneno", 45, 49, 49, 45, 1)
p2 = Pokemon(4, "Charmander", "Fuego", "", 39, 52, 43, 65, 1)

print(p1)
print(p2)