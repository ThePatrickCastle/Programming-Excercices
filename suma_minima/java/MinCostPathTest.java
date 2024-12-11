import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
class MinCostPathTest {
    @Test
     void minCostPath1() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix1 = {
                {1, 2, 3},
                {4, 5, 6},
                {7, 8, 9}
        };
        int camino = minCostPath.min_cost_path(matrix1);

        Assertions.assertEquals(21, camino);
    }


    @Test
    void minCostPath2() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix2 = {
                {9, 8, 7},
                {6, 5, 4},
                {3, 2, 1}
        };
        int camino = minCostPath.min_cost_path(matrix2);

        Assertions.assertEquals(21, camino);
    }
    @Test
    void minCostPath3() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix3 = {
                {1, 3, 5},
                {2, 4, 6},
                {7, 8, 9}
        };
        int camino = minCostPath.min_cost_path(matrix3);

        Assertions.assertEquals(22, camino);
    }

    @Test
    void minCostPath4() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix4 = {
                {9, 7, 5},
                {8, 6, 4},
                {3, 1, 2}
        };
        int camino = minCostPath.min_cost_path(matrix4);

        Assertions.assertEquals(23, camino);
    }

    @Test
    void minCostPath5() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix5 = {
                {10, 11, 12},
                {13, 14, 15},
                {16, 17, 18}
        };

        int camino = minCostPath.min_cost_path(matrix5);

        Assertions.assertEquals(66, camino);
    }

    @Test
    void minCostPath6() {
        MinCostPath minCostPath = new MinCostPath();
        int[][] matrix6 = {
                {42} // 1x1 matrix
        };

        int camino = minCostPath.min_cost_path(matrix6);
        Assertions.assertEquals(42, camino);
    }

  
}
