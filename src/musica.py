def duracion_a_segundos(tiempo_str):
    """Convierte un string 'm:ss' a un entero de segundos totales."""
    # Usamos split(':') para separar minutos y segundos
    partes = tiempo_str.split(':')
    minutos = int(partes[0])
    segundos = int(partes[1])
    return (minutos * 60) + segundos

def procesar_playlist(playlist):
    """Calcula el tiempo total, la canción más larga y la más corta."""
    total_segundos = 0
    # Inicializamos con la primera para comparar
    mas_larga = playlist[0]
    mas_corta = playlist[0]

    for cancion in playlist:
        # Accedemos a la duración en el diccionario
        segundos_actual = duracion_a_segundos(cancion["duration"])
        total_segundos += segundos_actual

        # Buscamos maximos y minimos
        if segundos_actual > duracion_a_segundos(mas_larga["duration"]):
            mas_larga = cancion
        if segundos_actual < duracion_a_segundos(mas_corta["duration"]):
            mas_corta = cancion

    # Convertimos el total de vuelta a formato 'Xm Ys'
    min_finales = total_segundos // 60
    seg_finales = total_segundos % 60
    
    return f"{min_finales}m {seg_finales}s", mas_larga, mas_corta