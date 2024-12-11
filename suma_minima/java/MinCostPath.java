/**
 * Ejercicicio. Trayectoria de costo minimo en una matriz.
 * @author Patricio Salvador Gonzalez Castillo No. Cuenta 32114239-1
 * @version 08.09.24.1
 **/
public class MinCostPath {
    /**
     * Método min_cost_path. Calcula la trayectoria de costo mínimo dada una matriz de valores enteros
     * @params matriz Con la que realizaremos los calculos
     * @return Último elemento de matriz "valores" con la trayectoria
     **/
    public int min_cost_path(int [][] matriz){
        // Usamos este arreglo para guardar la trayectoria de minimo costo hacia todos los elementos
        int [][] valores = new int[matriz.length][matriz[0].length];

        // Rellenamos la primera fila y columna pues solo hay una forma de llegar a ellas (Todo hacia abajo o todo hacia la derecha)
        int suma_fila = 0;
        for(int i = 0; i < matriz.length; i++){
            suma_fila += matriz[0][i];
            valores[0][i] = suma_fila;
        }
        int suma_columnas = 0;
        for(int i = 0; i < matriz[0].length; i++){
            suma_columnas += matriz[i][0];
            valores[i][0] = suma_columnas;
        }

        // Los demás elementos se calculan eligiendo min{elemento arriba, elemento a la izquierda}
        for(int i = 1; i < matriz.length; i++){
            for(int j = 1; j < matriz[0].length; j++){
                valores[i][j] = matriz[i][j] + Math.min(valores[i-1][j], valores[i][j-1]);
            }
        }
        return valores[matriz.length - 1][matriz[0].length - 1];
    }
}
