def peso_zona(peso, zona):
    """Calcula el costo de envío basado en 
    peso y zona."""
    zona = zona.strip().lower()
    tarifas = {"local": [500, 1000, 2000],
            "regional": [1000, 2500, 5000],
            "nacional": [2000, 4500, 8000]}
    if zona not in tarifas:
        return False
    #Determino el índice del precio según el peso
    if peso <= 1:
        indice = 0
    elif peso <= 5:
        indice = 1
    else:
        indice = 2
    precio_por_kg = tarifas[zona][indice]
    return precio_por_kg * peso