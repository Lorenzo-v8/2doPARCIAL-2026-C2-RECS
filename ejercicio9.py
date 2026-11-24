import csv
import os
from ejercicio1 import Cancion
from ejercicio2 import Biblioteca

ENCABEZADO = ["id", "titulo", "artista", "album", "genero", "anio", "duracion_seg"]


class ArchivoInvalidoError(Exception):
    pass

def guardar_canciones_csv(ruta, biblioteca):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(ENCABEZADO)
        for c in biblioteca:
            escritor.writerow([c.id, c.titulo, c.artista, c.album, c.genero, c.anio, c.duracion_seg])


def cargar_canciones_csv(ruta):
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe")

    biblioteca = Biblioteca()
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.reader(archivo)

        encabezado = next(lector, None)
        if encabezado != ENCABEZADO:
            raise ArchivoInvalidoError("El encabezado no es el pedido")

        for fila in lector:
            if len(fila) < 7:
                raise ArchivoInvalidoError(f"Una fila tiene {len(fila)} columnas y se esperaban 7")
            cancion = Cancion(int(fila[0]), fila[1], fila[2], fila[3], fila[4],
                              int(fila[5]), int(fila[6]))
            biblioteca.agregar(cancion)
    return biblioteca



# si, hay que recorrer las anteriores, cada fila es texto de largo variable, asi que no se puede calcular en que byte empieza la fila 50 y hay que ir
# leyendo y contando saltos de linea