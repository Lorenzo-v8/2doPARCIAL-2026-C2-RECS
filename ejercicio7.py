from ejercicio2 import CancionNoEncontradaError


class CampoInvalidoError(Exception):
    pass


def busqueda_lineal(canciones, campo, valor):
    if campo != "titulo" and campo != "artista" and campo != "genero":
        raise CampoInvalidoError(f"Campo '{campo}' invalido: usar 'titulo', 'artista' o 'genero'")

    encontradas = []
    for cancion in canciones:
        if getattr(cancion, campo) == valor:
            encontradas.append(cancion)
    return encontradas


def busqueda_binaria_por_titulo(canciones_ordenadas, titulo):
    inicio = 0
    fin = len(canciones_ordenadas) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        actual = canciones_ordenadas[medio]
        if actual.titulo == titulo:
            return actual
        elif actual.titulo < titulo:
            inicio = medio + 1
        else:
            fin = medio - 1

    raise CancionNoEncontradaError(f"No hay ninguna cancion con el titulo '{titulo}'")


#la busqueda binaria pide la lista ordenada por titulo porque en cada paso compara con el elemento del medio y descarta una mitad entera, 
#si el titulo buscado es menor, asume que esta a la izquierda; si es mayor, a la derecha.
#eso solo es cierto si la lista esta ordenada; en un caso contrario, podria descartar la mitad donde si estaba y tendriamos un problema.
#complejidad: la binaria es O(log n), porque en cada paso se reduce a la mitad. La lineal por artista es O(n) 
#tiene que mirar las n canciones (aunque encuentre una, debe seguir porque devuelve todas las coincidencias).