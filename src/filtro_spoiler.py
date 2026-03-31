def palabras_filtradas(texto, lista_spoilers):
    """Filtra spoilers sin usar expresiones regulares.
    Utiliza slicing e índices para mantener la integridad del texto."""
    texto_final = texto
    
    for p in lista_spoilers:
        palabra = p.strip()
        if not palabra:
            continue
        # Necesito un bucle while porque una palabra puede aparecer muchas veces en el texto.
        while True:
            # Busco la posición de la palabra en la versión minúscula del texto
            indice_inicio = texto_final.lower().find(palabra.lower())
            if indice_inicio == -1:
                break
            # Calculamos dónde termina la palabra
            indice_fin = indice_inicio + len(palabra)        
            # Reconstruyo el string usando SLICING
            texto_final = (texto_final[:indice_inicio] + "*" * len(palabra) + 
                texto_final[indice_fin:])
    
    return texto_final