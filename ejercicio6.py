from ejercicio4 import ListaEnlazada

class ColaVaciaError(Exception):
    pass

class Cola:
    def __init__(self):
        self._lista = ListaEnlazada()

    def encolar(self, dato):
        self._lista.insertar_al_final(dato)

    def desencolar(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No se puede desencolar, la cola esta vacia")
        return self._lista.quitar_primero()

    def ver_frente(self):
        if self._lista.esta_vacia():
            raise ColaVaciaError("No hay frente, la cola esta vacia")
        return self._lista.ver_primero()

    def esta_vacia(self):
        return self._lista.esta_vacia()

class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def siguiente(self):
        return self._cola.desencolar()

    def que_sigue(self):
        return self._cola.ver_frente()

#el primer siguiente() devuelve "Jijiji", porque la cola es FIFO (el primero que entra es el primero que sale).
#en la pila del ejercicio 5 pasaba al reves, con los mismos tres datos, el primer anterior() devolvia "De Musica Ligera",eso se explica por LIFO