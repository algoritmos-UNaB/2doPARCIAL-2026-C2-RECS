class Cancion:
    def __init__(self, id, titulo, artista, album, genero, anio, duracion_seg):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.genero = genero
        self.anio = anio
        self.duracion_seg = duracion_seg
    def duracion_mmss(self):
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"
    def __str__(self):
        return f"#{self.id} {self.titulo} - {self.artista} - {self.anio} - {self.duracion_mmss()}"
    def __eq__(self, otro):
        if not isinstance(otro, Cancion):
            return False
        return self.id == otro.id
'''
TEORÍA

Guardar la duración en segundos como entero hace mucho más fácil sumar tiempos, 
calcular promedios o filtrar canciones sin tener que andar partiendo strings cada vez.
Además, tenés el dato crudo separado de cómo se muestra, así que si mañana querés cambiar de m:ss a hh:mm:ss no tocás la información original
'''