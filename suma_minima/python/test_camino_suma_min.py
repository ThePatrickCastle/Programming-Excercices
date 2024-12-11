import pytest
from camino_suma_min import MinCostPath 

def test_min_cost_path1():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    camino = MinCostPath.min_cost_path(matrix1)
    assert camino == 21

def test_min_cost_path2():
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    camino = MinCostPath.min_cost_path(matrix2)
    assert camino == 21

def test_min_cost_path3():
    matrix3 = [
        [1, 3, 5],
        [2, 4, 6],
        [7, 8, 9]
    ]
    camino = MinCostPath.min_cost_path(matrix3)
    assert camino == 22

def test_min_cost_path4():
    matrix4 = [
        [9, 7, 5],
        [8, 6, 4],
        [3, 1, 2]
    ]
    camino = MinCostPath.min_cost_path(matrix4)
    assert camino == 23

def test_min_cost_path5():
    matrix5 = [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
    camino = MinCostPath.min_cost_path(matrix5)
    assert camino == 66

def test_min_cost_path6():
    matrix6 = [
        [42]  # Matriz 1x1
    ]
    camino = MinCostPath.min_cost_path(matrix6)
    assert camino == 42

def test_min_cost_path_7():
    matrix7 = [
        [74, 33, 50, 41, 22, 47, 66, 28, 76, 14, 92, 95, 3, 60, 5],
        [53, 47, 87, 81, 48, 64, 13, 30, 29, 59, 50, 78, 46, 37, 84],
        [98, 63, 45, 40, 70, 72, 49, 90, 56, 4, 28, 52, 19, 80, 82],
        [6, 29, 85, 69, 11, 91, 100, 48, 58, 73, 25, 39, 87, 53, 62],
        [95, 2, 43, 44, 32, 82, 51, 17, 61, 16, 12, 3, 65, 66, 26],
        [13, 23, 55, 68, 54, 47, 64, 39, 74, 31, 92, 70, 87, 6, 14],
        [50, 37, 82, 24, 96, 8, 85, 53, 79, 29, 41, 77, 32, 20, 11],
        [18, 21, 47, 14, 78, 12, 63, 32, 84, 54, 67, 22, 49, 89, 94],
        [64, 39, 52, 29, 15, 88, 20, 41, 16, 30, 77, 57, 93, 64, 60],
        [43, 17, 85, 88, 77, 94, 31, 20, 61, 98, 69, 26, 95, 41, 58],
        [91, 82, 64, 5, 37, 70, 93, 30, 22, 58, 46, 79, 9, 71, 12],
        [45, 63, 18, 31, 76, 22, 58, 94, 5, 28, 50, 90, 71, 62, 47],
        [78, 43, 26, 55, 81, 11, 64, 35, 97, 86, 28, 4, 22, 39, 67],
        [23, 98, 67, 51, 14, 43, 76, 58, 32, 49, 71, 16, 9, 6, 84],
        [12, 65, 89, 6, 43, 55, 91, 48, 27, 80, 6, 10, 64, 39, 32]
    ]
    camino = MinCostPath.min_cost_path(matrix7)
    assert camino == 862
    
def test_min_cost_path8():
    matrix8 = [
        [1, 1, 2, 2],
        [1, 1, 3, 6],
        [5, 10, 1, 1],
        [7, 7, 4, 1]
    ]
    camino = MinCostPath.min_cost_path(matrix8)
    assert camino == 9
