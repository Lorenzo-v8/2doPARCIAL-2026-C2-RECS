import os
import struct
from ejercicio1 import Cancion
from ejercicio2 import Biblioteca
from ejercicio9 import ArchivoInvalidoError

MAGIA = b"AYED"
TEMA = b"M"
FORMATO_ENCABEZADO = "=4s1sI"
FORMATO_REGISTRO = "=I40s40s40s16sHH"
TAM_ENCABEZADO = struct.calcsize(FORMATO_ENCABEZADO) 
TAM_REGISTRO = struct.calcsize(FORMATO_REGISTRO)      

def _a_bytes(texto, ancho):
    """UTF-8, recortado al ancho y completado con \\0."""
    datos = texto.encode("utf-8")[:ancho]
    return datos.ljust(ancho, b"\0")


def _a_texto(datos):
    """Corta en el primer \\0 y decodifica."""
    sin_relleno = datos.split(b"\0")[0]
    return sin_relleno.decode("utf-8", errors="ignore")


def _empaquetar(cancion):
    return struct.pack(FORMATO_REGISTRO,
                       cancion.id,
                       _a_bytes(cancion.titulo, 40),
                       _a_bytes(cancion.artista, 40),
                       _a_bytes(cancion.album, 40),
                       _a_bytes(cancion.genero, 16),
                       cancion.anio,
                       cancion.duracion_seg)


def _desempaquetar(datos):
    id, titulo, artista, album, genero, anio, duracion = struct.unpack(FORMATO_REGISTRO, datos)
    return Cancion(id, _a_texto(titulo), _a_texto(artista), _a_texto(album),
                   _a_texto(genero), anio, duracion)


def _validar_y_leer_cantidad(ruta):
    """Valida el archivo y devuelve la cantidad de registros."""
    if not os.path.exists(ruta):
        raise ArchivoInvalidoError(f"El archivo '{ruta}' no existe")

    tamanio = os.path.getsize(ruta)
    if tamanio < TAM_ENCABEZADO:
        raise ArchivoInvalidoError("El archivo es mas chico que el encabezado")

    with open(ruta, "rb") as archivo:
        magia, tema, cantidad = struct.unpack(FORMATO_ENCABEZADO, archivo.read(TAM_ENCABEZADO))

    if magia != MAGIA:
        raise ArchivoInvalidoError("La magia del archivo no es AYED")
    if tema != TEMA:
        raise ArchivoInvalidoError("El tema del archivo no es M")
    if tamanio != TAM_ENCABEZADO + cantidad * TAM_REGISTRO:
        raise ArchivoInvalidoError("El tamanio del archivo no coincide con la cantidad de registros")
    return cantidad


def guardar_binario(ruta, biblioteca):
    with open(ruta, "wb") as archivo:
        archivo.write(struct.pack(FORMATO_ENCABEZADO, MAGIA, TEMA, biblioteca.cantidad()))
        for cancion in biblioteca:
            archivo.write(_empaquetar(cancion))


def cargar_binario(ruta):
    cantidad = _validar_y_leer_cantidad(ruta)
    biblioteca = Biblioteca()
    with open(ruta, "rb") as archivo:
        archivo.seek(TAM_ENCABEZADO)
        for i in range(cantidad):
            datos = archivo.read(TAM_REGISTRO)
            biblioteca.agregar(_desempaquetar(datos))
    return biblioteca


def actualizar_registro(ruta, posicion, cancion):
    cantidad = _validar_y_leer_cantidad(ruta)
    if posicion < 0 or posicion >= cantidad:
        raise ArchivoInvalidoError(f"La posicion {posicion} esta fuera de rango (hay {cantidad} registros)")

    with open(ruta, "r+b") as archivo:
        archivo.seek(TAM_ENCABEZADO + posicion * TAM_REGISTRO)
        archivo.write(_empaquetar(cancion))  
# El registro de posicion k (0-based) empieza en el byte:
#     inicio_k = TAM_ENCABEZADO + k * TAM_REGISTRO = 9 + k * 144
# Por ejemplo, el registro 0 empieza en el byte 9 y el registro 3 en
# 9 + 3 * 144 = 441. Como todos miden lo mismo, se puede hacer seek directo
# sin leer los anteriores.