def ordenar_por_anio_seleccion(canciones):
    n = len(canciones)
    for i in range(n - 1):
        pos_mayor = i
        for j in range(i + 1, n):
            if canciones[j].anio > canciones[pos_mayor].anio:
                pos_mayor = j
        auxiliar = canciones[i]
        canciones[i] = canciones[pos_mayor]
        canciones[pos_mayor] = auxiliar
    return canciones


def ordenar_por_duracion_insercion(canciones):
    for i in range(1, len(canciones)):
        actual = canciones[i]
        j = i - 1
        while j >= 0 and canciones[j].duracion_seg > actual.duracion_seg:
            canciones[j + 1] = canciones[j]
            j -= 1
        canciones[j + 1] = actual
    return canciones

# en el peor caso las dos son O(n^2). seleccion siempre hace unas n^2/2 comparaciones, sin importar como venga la lista, 
#insercion llega a n^2 cuando la lista viene ordenada al reves.
# la que conserva el orden de claves iguales (osea estable) es insercion: solo corre elementos que son estrictamente mayores, 
#asi que dos canciones con la misma duracion nunca se cruzan. seleccion no es estable, porque el intercambio puede mandar un elemento por encima de otro igual.