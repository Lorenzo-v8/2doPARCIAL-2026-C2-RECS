# A continuacion escribo primero el codigo respondiendo el ejercicio, en el final del codigo de este ejercicio esta escrita la respuesta teorica
# las consignas no considere correcto volver a copiarlas

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
        return f"#{self.id} {self.titulo} | {self.artista} | {self.anio} | {self.duracion_mmss()}"

    def __eq__(self, otra):
        if not isinstance(otra, Cancion):
            return False
        return self.id == otra.id




# Respuesta a la teoria

# La duracion se guarda como entero en segundos porque con al ser un numero, nos permite sumar, comparar y ordenar, la duracion total de una playlist me parece un buen ejemplo.
#El formato "m:ss" es solo una forma de mostrarlo, por eso se calcula en duracion_mmss cuando es necesario;
#en un caso como string 5:16 habria que convertilo cada vez que queramos operar con el lo que lo haria muy tedioso
