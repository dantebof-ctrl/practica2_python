def procesar_mensaje(mensaje, desplazamiento):
    """Aplica el cifrado César a un mensaje. 
    Mantiene símbolos y respeta mayúsculas/minúsculas."""
    resultado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            base = ord('A') if caracter.isupper() else ord('a')
            # Aplico formula que saque de internet porque no me salia
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            # Si no es letra (espacio, !, 1), se queda igual
            resultado += caracter
            
    return resultado