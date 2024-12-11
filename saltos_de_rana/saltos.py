"""
Ejercicio 3 de Laboratorio. Saltos
Author: Patricio Salvador González Castillo
No. Cuenta: 32114239-1
Version 1.0

"""

def saltos(arreglo):
    """
    Funcion saltos. Determina si es posible alcanzar el último elemento del arreglo "saltando" los indices
    
    Args:
    arreglo (array): El arreglo a determinar

    Returns:
    True/False (Bool): Verdadero si se puede alcanzar el indice final, falso si no

    """
    
    distanciaMaximaRecorrible = 0
    longitudArreglo = len(arreglo)
    for i in range(longitudArreglo):
        if distanciaMaximaRecorrible >= i:
            distanciaLocal = i + arreglo[i]
            if distanciaLocal > distanciaMaximaRecorrible:
                distanciaMaximaRecorrible = distanciaLocal
            if distanciaMaximaRecorrible >= longitudArreglo - 1:
                return True
        else:
            return False
    return False

        
