def procesar_competencia(rondas):
    acumulado = {}
    contador = 1
    for ronda in rondas:
        print(f"Ronda {contador}- {ronda['theme']}")
        contador += 1
        puntajes_ronda = {} # Para calcular el ganador de ESTA ronda
        for nombre, jueces in ronda['scores'].items():
            #Sumo los puntos de los 3 jueces
            puntos_totales = sum(jueces.values())
            puntajes_ronda[nombre] = puntos_totales
            #Inicializo o actualo el acumulado general
            if nombre not in acumulado:
                acumulado[nombre] = {'total': 0, 'ganadas': 0, 'mejor': 0, 'cant': 0}
            acumulado[nombre]['total'] += puntos_totales
            acumulado[nombre]['cant'] += 1  #para luego sacar el promedio 
            # Verifo si es su mejor marca personal
            if puntos_totales > acumulado[nombre]['mejor']:
                acumulado[nombre]['mejor'] = puntos_totales
        #Determino el ganador de la ronda
        ganador_ronda = max(puntajes_ronda, key=puntajes_ronda.get)
        puntos_ganador = puntajes_ronda[ganador_ronda]
        acumulado[ganador_ronda]['ganadas'] += 1
        print(f" Ganador: {ganador_ronda} ({puntos_ganador} pts)")
        #Creo el ranking de la ronda ordenado
        #Ordenamos por el valor (x[1]) de forma descendente (reverse=True)
        ranking_ronda = sorted(puntajes_ronda.items(), key=lambda x: x[1], reverse=True)

        #Imprimimos la tabla de esta ronda específica
        print(f"\n--- Tabla de Posiciones: {ronda['theme']} ---")
        print(f"{'Puesto':<8} {'Cocinero':<12} {'Puntaje'}")
        for puesto, (nombre, puntos) in enumerate(ranking_ronda,1):
        # El primero de la lista es el ganador que ya calculamos
            print(f"{puesto:<8} {nombre:<12} {puntos}")
        print("-" * 30)
    return acumulado

def imprimir_tabla_final(acumulado):
    #Convierto a lista y ordenamos por 'total' de forma descendente
    ranking = sorted(acumulado.items(), key=lambda x: x[1]['total'], reverse=True)
    print("\n" + "="*70)
    print("TABLA DE POSICIONES FINAL:")
    print(f"{'Cocinero':<15} {'Puntaje':<10} {'Ganadas':<10} {'Mejor':<10} {'Promedio':<10}")
    print("-" * 70)

    for nombre, datos in ranking:
        promedio = datos['total'] / datos['cant']
        print(f"{nombre:<15} {datos['total']:<10} {datos['ganadas']:<10} "
              f"{datos['mejor']:<10} {promedio:<10.1f}")
    print("="*70)