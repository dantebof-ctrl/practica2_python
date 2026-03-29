def analizar_zen(texto):
    """Calcula estadísticas del texto recibido.
    Retorna una tupla con los resultados."""
    # Separamos por líneas y limpiamos espacios vacíos con la funcion strip
    lineas=texto.split('\n')
    total_lineas=len(lineas)
    
    # Contamos palabras por cada línea
    palabras_por_linea=[]
    for linea in lineas:
        palabras_por_linea.append(len(linea.split()))
    total_palabras = sum(palabras_por_linea)

    promedio = total_palabras / total_lineas
    
    # Retornamos múltiples valores (esto devuelve una tupla)
    return total_lineas, total_palabras, promedio, lineas, palabras_por_linea