from ejercicio2 import CancionNoEncontradaError

class ListaVaciaError(Exception):
    pass

class Nodo:
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self._primero = None

    def esta_vacia(self):
        return self._primero is None

    def tamanio(self):
        contador = 0
        actual = self._primero
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def insertar_al_inicio(self, dato):
        self._primero = Nodo(dato, self._primero)

    def insertar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self._primero is None:
            self._primero = nuevo
        else:
            actual = self._primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def quitar_primero(self):
        if self._primero is None:
            raise ListaVaciaError("no se puede sacar el primero de una lista vacia")
        dato = self._primero.dato
        self._primero = self._primero.siguiente
        return dato

    def ver_primero(self):
        if self._primero is None:
            raise ListaVaciaError("la lista esta vacia")
        return self._primero.dato

    def quitar(self, dato):
        if self._primero is None:
            return False
        if self._primero.dato == dato:
            self._primero = self._primero.siguiente
            return True
        anterior = self._primero
        while anterior.siguiente is not None:
            if anterior.siguiente.dato == dato:
                anterior.siguiente = anterior.siguiente.siguiente
                return True
            anterior = anterior.siguiente
        return False

    def __iter__(self):
        actual = self._primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


class Playlist:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def quitar(self, id):
        for cancion in self._canciones:
            if cancion.id == id:
                self._canciones.quitar(cancion)
                return cancion
        raise CancionNoEncontradaError(f"La cancion con id {id} no esta en la playlist")

    def listar(self):
        resultado = []
        for cancion in self._canciones:
            resultado.append(str(cancion))
        return resultado

    def duracion_total(self):
        total = 0
        for cancion in self._canciones:
            total += cancion.duracion_seg
        return total

# Como la lista solo guarda la referencia al primer nodo, para insertar al final hay que recorrer todos los nodos hasta llegar al ultimo
#osea que con n elementos se recorren los n nodos, por lo tanto la operacion es O(n).