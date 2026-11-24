def versiones_de(biblioteca, versiones, cancion_id):
    biblioteca.obtener(cancion_id)

    directas = []
    for v in versiones:
        if v[1] == cancion_id:
            directas.append(v)
    directas = sorted(directas, key=lambda v: v[0])

    resultado = []
    for v in directas:
        cancion = biblioteca.obtener(v[0])
        resultado.append((cancion.titulo, v[2]))
        resultado = resultado + versiones_de(biblioteca, versiones, v[0])
    return resultado


# El caso base es cuando nadie es version de la cancion que estoy mirando, por ejemplo, no hay ninguna tupla con ese id en version_de_id, entonces devuelvo [].
# Para versiones_de(..., 12):
# - versiones_de(12): la unica version directa es la 13 (live). Guardo ("Ji Ji Ji", "live") y me fijo que cuelga de la 13 llamando a versiones_de(13).
# - versiones_de(13): la unica directa es la 70 (remix). Guardo ("Ji Ji Ji (Remix)", "remix") y llamo a versiones_de(70).
# - versiones_de(70): nadie es version de la 70, asi que es el caso base y devuelve [].
# Ahora se vuelve para atras, y cada llamada junta su propia tupla con lo que le devolvio la de abajo:
# - la 13 devuelve [("Ji Ji Ji (Remix)", "remix")] + [] = [("Ji Ji Ji (Remix)", "remix")]
# - la 12 devuelve [("Ji Ji Ji", "live")] + lo que obtuvimos de la 13 = [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")]
# Por eso queda en preorden: primero la version directa y despues lo que cuelga de ella.