class Cancion:
    def __init__(self, id: int, titulo: str, artista: str, album: str, genero: str, anio: int, duracion_seg: int):
        self.id = int(id)
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = int(anio)
        self.duracion_seg = int(duracion_seg)

    def duracion_mmss(self) -> str:
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self) -> str:
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, otro) -> bool:
        if not isinstance(otro, Cancion):
            return False
        return self.id == otro.id


if __name__ == "__main__":
    c = Cancion(12, "Jijiji", "Patricio Rey y sus Redonditos de Ricota", "Un Baion para el Ojo Idiota", "Rock", 1988, 316)
    print(c)
    assert c.duracion_mmss() == "5:16"
    assert Cancion(1, "A", "B", "C", "D", 2000, 65).duracion_mmss() == "1:05"
    assert Cancion(2, "A", "B", "C", "D", 2000, 59).duracion_mmss() == "0:59"

# Teoria:
# Guardar la duracion en segundos enteros permite realizar calculos aritmeticos directos (como sumar duraciones
# totales o comparar cual cancion es mas larga) y ocupa menos memoria que una cadena de texto.
# En cambio, si se guardara como string ("5:16"), habria que parsear y convertir el texto cada vez que se necesite operar matematicamente con el tiempo.