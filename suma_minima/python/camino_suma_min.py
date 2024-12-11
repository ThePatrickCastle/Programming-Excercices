"""
Ejercicio 3. Trayectoria de costo minimo en una matriz cuadrada de numeros positivos
Author: Patricio Salvador González Castillo
Version 1.0.1
"""

class MinCostPath():
    '''
    Clase MinCostPath. Calcula la trayectoria de costo mínimo dada una matriz de valores enteros
    
    Metodos
    -------
    * min_cost_path(matriz) 

    '''
    def min_cost_path(matriz):
        # Usamos este arreglo para guardar la trayectoria de mínimo costo hacia todos los elementos
        valores = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]
        
        # Rellenamos la primera fila y columna
        suma_fila = 0
        for i in range(len(matriz[0])):
            suma_fila += matriz[0][i]
            valores[0][i] = suma_fila
            
        suma_columnas = 0
        for i in range(len(matriz)):
            suma_columnas += matriz[i][0]
            valores[i][0] = suma_columnas
            
        # Calculamos los demás elementos eligiendo min(elemento arriba, elemento a la izquierda)
        for i in range(1, len(matriz)):
            for j in range(1, len(matriz[0])):
                valores[i][j] = matriz[i][j] + min(valores[i-1][j], valores[i][j-1])

        return valores[len(matriz) - 1][len(matriz[0]) - 1]


