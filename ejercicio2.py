
class CancionNoEncontradaError(Exception):
    pass


class Biblioteca:
    def __init__(self):
        self._canciones = []

    def agregar(self, cancion):
        self._canciones.append(cancion)

    def cantidad(self):
        return len(self._canciones)

    def obtener(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                return cancion
        raise CancionNoEncontradaError(f"No existe una cancion con id {id} en la biblioteca")

    def listar(self):
        resultado = []
        for cancion in self._canciones:
            resultado.append(str(cancion))
        return resultado

    def __iter__(self):
        return iter(self._canciones)

# Respuesta a la teoria:
# La biblioteca guarda el catalogo completo de canciones (todas las que existen). 
#en cambio una playlist guarda solo la seleccion de canciones que el usuario haya eligido, en un orden determinado, y puede ser distinta de otra playlist.