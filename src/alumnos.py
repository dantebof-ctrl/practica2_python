def limpiar_registros(lista_alumnos):
    """Limpia, normaliza y elimina duplicados quedándose con la nota máxima. """
    # Usao un diccionario donde la clave sea el NOMBRE normalizado
    alumnos_limpios = {}

    for registro in lista_alumnos:
        name = registro.get("name")
        grade = registro.get("grade")
        status = registro.get("status")
        if not name or not name.strip():
            continue
            
        #Uso isdigit() porque las notas vienen como strings "8"
        if grade is None or not str(grade).isdigit():
            continue
            
        nombre_norm = name.strip().title()
        estado_norm = status.strip().title() if status else "Desconocido"
        nota_int = int(grade)

        if nombre_norm not in alumnos_limpios:
            #Si no está, lo agrego
            alumnos_limpios[nombre_norm] = {"nota": nota_int, "estado": estado_norm}
        else:
            #Si ya está, comparo notas
            if nota_int > alumnos_limpios[nombre_norm]["nota"]:
                alumnos_limpios[nombre_norm]["nota"] = nota_int
                # Actualizamos estado por las dudas
                alumnos_limpios[nombre_norm]["estado"] = estado_norm

    listado_final = sorted(alumnos_limpios.items())
    
    return listado_final