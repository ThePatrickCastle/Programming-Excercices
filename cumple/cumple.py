'''Dos amigos, Juan y Diego, quieren compartir una barra de chocolate. 
Cada uno de los cuadrados de la barra tiene un número entero.
Juan decide compartir un segmento contiguo de la barra seleccionada de modo que:

*La longitud del segmento coincida con el mes de nacimiento de Diego y,
*La suma de los números enteros en los cuadrados sea igual a su día de nacimiento.

Completa la función cumple, esta debe determinar de cuántas maneras puede dividir 
el chocolate.

Entrada: Un arreglo que simule la barra de chocolate c, 
d es el día de nacimiento de Diego
m es el mes de nacimiento de Diego

Salida: Un entero que representa el número de segmentos que Juan puede seleccionar
para dividir la barra de chocolate.

Por ejemplo:
Dado el arreglo para simular la barra de chocolate c = [1, 2, 1, 3, 2, 2, 1]
el día de cumpleaños d = 3
y el mes de cumpleaños m = 2

Juan puede dividir la barra en 3 segmentos que cumplen con las condiciones:
[1,2], [2,1] y [2,1]

Ejemplo 2:
Dado el arreglo para simular la barra de chocolate c = [4, 1, 2, 1, 3, 2]
el día de cumpleaños d = 5
y el mes de cumpleaños m = 2
Juan puede dividir la barra en 2 segmentos que cumplen con las condiciones:
[1,4] y [3,2]
'''

"""
El problema nos pide encontrar el numero de cadenas de longitud m cuya suma 
de elementos sea igual a d. Lo resolví iterando sobre la lista 2 veces: en 
el ciclo interno se suman los elementos consecutivos m veces y en el externo se
recorre cada posible suma consecutiva.
"""
def cumple(c, d, m):
    ctam = len(c) # Usamos len() para determinar el tamaño de la lista
    no_segmentos = 0 # Inicializamos en 0 el numero de cadenas que cumplen la condicion 
    for i in range(0, ctam-m+1): # Iteramos sobre la lista menos el tamaño de m pues sumas consecutivas de menor longitud no aplican
        suma_elementos = 0 # Cada iteración reiniciamos la variable que contiene la suma de cadenas de longitud m
        for j in range(i, i+m): # Aqui sucede la magia! En el segundo ciclo acumulamos la suma desde el pivote hasta el pivote + m
            suma_elementos += c[j]
        if suma_elementos == d: # Verificamos condicion y de cumplirse sumamos 1 al numero de segmentos    
            no_segmentos += 1
    return no_segmentos # Regresamos el numero ded segmentos que cumplen la condicion