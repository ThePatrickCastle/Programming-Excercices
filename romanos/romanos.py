"""
Ejercicio 5. numerosRomanos
Author: Patricio Salvador González Castillo
No. Cuenta: 32114239-1
Version 1.0.0

"""

'''Dado un número romano, conviértelo a un número entero. '''
def numerosRomanos(s):
    diccionarioRomanos = {'I': 1,
                          'V': 5,
                          'X': 10,
                          'L': 50,
                          'C': 100,
                          'D': 500,
                          'M': 1000}

    longitud_cadena = len(s)
    resultado = 0
    i = 0

    while i < longitud_cadena:
        primero = diccionarioRomanos.get(s[i])

        if i+1 < longitud_cadena:
            segundo = diccionarioRomanos.get(s[i+1])
            if (primero < segundo):
                resultado += segundo - primero
                i += 2
            else:
                resultado += primero
                i += 1
        else:
            resultado += primero
            i += 1

    return resultado




